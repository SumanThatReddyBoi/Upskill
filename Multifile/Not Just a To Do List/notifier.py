import smtplib
from email.message import EmailMessage
import datetime as dt

now = dt.datetime.now()
mail_now = now.strftime("%d-%m-%Y %H:%M:%S")

def alerter(to, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = f"Your To Do List - Export '{mail_now}'"
    msg['to'] = to

    user = "" #removed due to security reasons
    msg['from'] = user
    password = "" #removed due to security reasons

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()
