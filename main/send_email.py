import smtplib
from email.mime.text import MIMEText

from settings import EMAIL_FROM


def new_user(user):
    text = f"""New user: id:{user.id} email:{user.email} name:{user.name}"""
    msg = MIMEText(text)

    msg['Subject'] = 'ZV :: ' + text
    msg['From'] = EMAIL_FROM
    msg['To'] = EMAIL_FROM

    with smtplib.SMTP('localhost') as smtp:
        smtp.sendmail(msg['From'], [msg['To']], msg.as_string())
