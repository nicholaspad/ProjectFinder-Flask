import smtplib
import ssl

import pytz

from models import *


def is_past_due():
    config = Config.query.first()
    return timezone("US/Eastern").localize(config.due_date) < datetime.now(
        tz=pytz.timezone("US/Eastern")
    )


def send_email(to_email, message, sender_pw):
    port = 587
    smtp_server = "smtp-mail.outlook.com"
    sender_email = EMAIL

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context)
        server.login(sender_email, sender_pw)
        server.sendmail(sender_email, to_email, message.strip())


def log_email(users, email_type):
    for user in users:
        EmailLog(
            user=user,
            date=datetime.now(tz=pytz.timezone("US/Eastern")),
            email_type=email_type,
        ).save()
