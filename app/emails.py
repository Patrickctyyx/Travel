from flask_mail import Message, Mail
from flask import current_app, render_template

mail = Mail()


def send_email(to, subject, template, **kwargs):
    msg = Message(current_app.config['FLASK_MAIL_SUBJECT_PREFIX'] + subject,
                  sender=current_app.config['FLASK_MAIL_SENDER'],
                  recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    mail.send(msg)
