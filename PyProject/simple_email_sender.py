# simple_email_sender.py
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, receiver_email, subject, body, smtp_server, port, login, password):
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    message.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(login, password)
        server.send_message(message)

if __name__ == "__main__":
    sender = 'your_email@example.com'
    receiver = 'receiver_email@example.com'
    subject = 'Test Email'
    body = 'This is a test email sent from Python.'
    smtp_server = 'smtp.example.com'
    port = 587
    login = 'your_email@example.com'
    password = 'your_password'

    send_email(sender, receiver, subject, body, smtp_server, port, login, password)
    print("Email sent successfully!")
