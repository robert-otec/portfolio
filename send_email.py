import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "test.robert.otec@gmail.com"
password = "ivkkeohifuzqgegy"

receiver = "robertotec@outlook.cz"
context = ssl.create_default_context()

message = """\
Subject: Test Email from Python Script
Hello,
testing email sending functionality.
Robert
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)