import smtplib
import ssl

# Replace these values with your own email/account details
sender_email = "your_email@gmail.com"
sender_password = "your_app_password"
receiver_email = "recipient@example.com"

subject = "Hello from Gmail SMTP"
body = "This is a test email sent from a Python script using Gmail SMTP."

message = f"Subject: {subject}\n\n{body}"

smtp_server = "smtp.gmail.com"
port = 465  # For SSL

context = ssl.create_default_context()

try:
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message)
    print("Email sent successfully.")
except Exception as e:
    print(f"Failed to send email: {e}")
