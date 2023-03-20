import imaplib
import email
from email.header import decode_header
import time
import os
import re


def checkmail():
    # account credentials
    username = "email"
    password = "password"

    # create an IMAP4 class with SSL
    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    # authenticate
    imap.login(username, password)

    # select the mailbox I want to delete in
    # if you want SPAM, use imap.select("SPAM") instead
    imap.select("INBOX")

    # search for specific mails by sender and subject
    search_query = 'FROM "wallace@golangdojo.com" UNSEEN'
    # search_query = 'FROM "wallace@golangdojo.com" SUBJECT "The last day"'
    # search_query = 'FROM "support@spamhaus.org" SUBJECT "Spamhaus removal verification for"'
    status, messages = imap.search(None, search_query)

    messages = messages[0].split(b' ')

    for mail in messages:
        if mail:
            _, msg = imap.fetch(mail, "(RFC822)")
            for response in msg:
                if isinstance(response, tuple):
                    msg = email.message_from_bytes(response[1])
                    # decode the email subject
                    subject = decode_header(msg["Subject"])[0][0]

                    if isinstance(subject, bytes):
                        subject = subject.decode()

                    print("Processing email with subject:", subject)

                    verifying_email = ""
                    payload = msg.get_payload()

                    if isinstance(payload, list):
                        # email contains multiple payloads (plaintext and HTML)
                        for part in payload:
                            if part.get_content_type() == "text/plain":
                                print(part.get_payload())
                                verifying_email_match = re.search(r"https://.*verification-token.*",
                                                                  part.get_payload())
                                if verifying_email_match:
                                    verifying_email = verifying_email_match.group()
                                    break

                    else:
                        # email contains only plaintext payload
                        verifying_email_match = re.search(r"https://.*verification-token.*", payload)
                        if verifying_email_match:
                            verifying_email = verifying_email_match.group()
                            break

                    print(f"Opening link: {verifying_email}")
                    os.system(f'start chrome "{verifying_email}"')

                    time.sleep(30)
                    os.popen(f"taskkill /im chrome.exe /f")

                    # mark the mail as deleted
                    if verifying_email:
                        print("deleted")
                        imap.store(mail, "+FLAGS", "\\Deleted")

    # permanently remove mails that are marked as deleted
    # from the selected mailbox (in this case, INBOX)
    imap.expunge()
    # close the mailbox
    imap.close()
    # logout from the account
    imap.logout()


while True:
    print("Checking mail")
    checkmail()
    print("Waiting for 30 seconds...")
    time.sleep(30)
