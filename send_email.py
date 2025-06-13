import smtplib, ssl
import os

print(os.getenv("PASSWORD"))  # For debugging purposes, remove in production

# This script sends an email using SMTP with SSL.
def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "test.robert.otec@gmail.com"
    password = os.getenv("PASSWORD")

    receiver = "robertotec@outlook.cz"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)