import os
import smtplib
import ssl
from email.message import EmailMessage

def send_email(receiver_email):
    with open(".env", "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            key, value = line.split("=")
            os.environ[key] = value

    # Set the subject and body of the email
    subject = 'Successful registration with!'
    body = """
    Dear User,

    Thank you for registering on our site. We're delighted to have you as a member of our community.

    Should you have any questions or need assistance, please feel free to reach out to us.








    Best regards,
    Joshua Musira.
    """

    em = EmailMessage()
    em['From'] = os.environ.get('EMAIL_SENDER')  # Access environment variable directly
    em['To'] = receiver_email
    em['Subject'] = subject
    em.set_content(body)

    # Add SSL (layer of security)
    context = ssl.create_default_context()

    # Log in and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        try:
            smtp.login(os.environ.get('EMAIL_SENDER'), os.environ.get('EMAIL_PASSWORD'))
            smtp.send_message(em)  # Use send_message() instead of sendmail()
            print("Welcome email sent to:", receiver_email)
        except smtplib.SMTPAuthenticationError as e:
            print("Error: Username and Password not accepted.")


