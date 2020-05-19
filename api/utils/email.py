from flask import current_app
from flask_mail import Mail,Message
mail = Mail()


def send_email(to,subject,template):
    message = Message(
        subject,
        recipients=[to],
        html=template,
        sender = current_app.config['MAIL_DEFAULT_SENDER']
    )
    mail.send(message)