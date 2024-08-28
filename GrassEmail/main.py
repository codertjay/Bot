import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, to_emails, from_email, smtp_server, smtp_port, login, password):


    # Create SMTP session
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure the connection
        server.login(login, password)

        # Send email to each recipient
        for email in to_emails:
            msg = MIMEMultipart()
            msg['From'] = from_email
            msg['To'] = email
            msg['Subject'] = subject

            html_body = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🚀 Last Chance to Join the IO.NET Airdrop! 🚀</title>
</head>
<body style="font-family: Arial, sans-serif; line-height: 1.6;">
<div style="max-width: 600px; margin: auto; padding: 20px; border: 1px solid #ddd; border-radius: 5px;">
    <h2 style="color: #2c3e50;">🎉 Don't Miss Out on the IO.NET Airdrop! 🎉</h2>
    <p>Hi there,</p>
    <p>Exciting news! <a href="https://t.me/Ionet_airdrop_bot?start=r09821783300" style=""> IO.NET</a> is launching its airdrop, and you're invited to participate!</p>
    <p>Here's why you should join:</p>
    <ul style="padding-left: 20px;">
        <li style="margin-bottom: 10px;">🚀 Get free 50 $IO tokens just for joining the airdrop!</li>
        <li style="margin-bottom: 10px;">💰 Earn additional rewards: Get 10 $IO for every valid referral!</li>
        <li style="margin-bottom: 10px;">💼 Top 50 referrers stand a chance to win up to $500 USDt!</li>
    </ul>
    <p>Hurry, this offer ends in less than 24 hours!</p>
    <p>End Time: 05:00 PM</p>
    <p>Notcoin has already paid out significant rewards to its users, and now IO.NET is partnering with Binance, offering even more lucrative rewards!</p>
    <p>Join now using the link below:</p>
    <p style="text-align: center;">
        <a href="https://t.me/Ionet_airdrop_bot?start=r09821783300" style="background-color: #2ecc71; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px;">Join IO.NET Airdrop</a>
    </p>
    <p>Don't miss out on this chance to earn valuable rewards! Get started now and be part of the IO.NET community!</p>
    <p>Best regards,</p>
    <p>{email}</p>
</div>
</body>
</html>
            """
            msg.attach(MIMEText(html_body, 'html'))

            text = msg.as_string()
            server.sendmail(from_email, email, text)
            print(f'Email sent to {email}')

        server.quit()
        print('All emails sent successfully.')

    except Exception as e:
        print(f'Failed to send email. Error: {str(e)}')

# Usage example
if __name__ == '__main__':
    subject = "💰🚀 Last Chance to Join the IO.NET Airdrop & Win Big Money! 🎉💰"


    from_email = "grasss.dev@gmail.com"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    login = "grasss.dev@gmail.com"
    password = "zpurfrcchxmkxotx"

    # Step 1: Open the file
    with open('mail.txt', 'r') as file:
        # Step 2: Read all lines of the file
        emails = file.readlines()

    # Step 3: Remove leading/trailing whitespaces from each email
    # to_emails = ["dev.codertjay@gmail.com", "codertjay@gmail.com"]
    to_emails = [email.strip() for email in emails]

    send_email(subject, to_emails, from_email, smtp_server, smtp_port, login, password)
