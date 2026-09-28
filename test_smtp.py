import smtplib, ssl
from email.message import EmailMessage

msg = EmailMessage()
msg.set_content("This is a test email from the lead scraper.")
msg["Subject"] = "Test Email"
msg["From"] = "christopher.oneal@szglabs.com"
msg["To"] = "christopher.oneal@szglabs.com"

try:
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("mail.privateemail.com", 465, context=context) as server:
        server.login("christopher.oneal@szglabs.com", "90()opOPl;L:")
        server.send_message(msg)
    print("Email sent successfully!")
except Exception as e:
    print("Error:", e)
