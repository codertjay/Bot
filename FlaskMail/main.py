from flask import Flask, request, jsonify
from flask_mail import Mail, Message
from decouple import config

app = Flask(__name__)

# Configure Flask-Mail -- Use your actual mail server settings
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = config("MAIL_USERNAME")
app.config['MAIL_PASSWORD'] = config("MAIL_PASSWORD")
app.config['MAIL_DEFAULT_SENDER'] = config("MAIL_USERNAME")

# Initialize Flask-Mail
mail = Mail(app)

def send_simple_email():
    msg = Message("Hello",
                  recipients=[config("RECIPIENT_EMAIL")],
                  body="This is a simple email sent from a Flask application!")
    with app.app_context():
        mail.send(msg)
        print("Simple email sent!")

# Route to trigger email send, now accepting both GET and POST methods
@app.route('/send_email', methods=['GET', 'POST'])
def trigger_email():
    send_simple_email()
    return "Email sent!"

if __name__ == '__main__':
    with app.app_context():
        send_simple_email()
    app.run(debug=True)
