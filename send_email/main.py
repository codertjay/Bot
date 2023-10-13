import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SMTP_USERNAME = '1xbetofficial00000@gmail.com'
SMTP_PASSWORD = 'smtlrszlstxeznls'

# Email content
subject = "Exciting Premier League Matches on 1xBet!"
message_template = """

<div class="separator" style="width: 100%;border-bottom: 2px solid #ddd;margin: 0 0;">
</div>
<header style="background-color: #f9f9f9;text-align: center;padding: 20px 0;">
    <img src="https://i.imgur.com/TPhez6J.png" alt="Logo" style="width: 150px;">
</header>
<div class="separator" style="width: 100%;border-bottom: 2px solid #ddd;margin: 0 0;">
</div>
<!-- Add your content below the separator -->
<p style="line-height: 1.6; padding-left: 20px; font-family: Arial, sans-serif; color: #333; font-size: 16px;">
    <strong style="color: #ff6600;">Bet on the legendary Premier League matches on 1xBet!</strong><br>
    Arsenal - Tottenham and Chelsea - Aston Villa matches will be this Sunday.<br><br>

    Register with this promo code <span style="color: #ff6600; font-weight: bold;">*</span> to get up to 300% bonus on
    your first deposit and enjoy other bonuses on 1xBet. You can predict the winner of the tournament right now!<br><br>

    Also, if you participate in “HYPER BONUS” promo, you will get up to 1000% on your winnings!
    Swipe up to register or
    <a href="https://bit.ly/3reMRtJ"
       style="color: #ff6600; text-decoration: none; font-weight: bold;">click this link</a> to register.
</p>

"""

# List of recipient email addresses
recipients = ['dev.codertjay@gmail.com']

# Create a connection to the SMTP server
with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
    server.starttls()
    server.login(SMTP_USERNAME, SMTP_PASSWORD)

    # Send the email to each recipient
    for recipient in recipients:
        msg = MIMEMultipart()
        msg['From'] = SMTP_USERNAME
        msg['To'] = recipient
        msg['Subject'] = subject

        # Create the HTML message
        message = MIMEText(message_template, 'html')
        msg.attach(message)

        # Send the email
        server.sendmail(SMTP_USERNAME, recipient, msg.as_string())

print("Emails sent successfully to all recipients!")
