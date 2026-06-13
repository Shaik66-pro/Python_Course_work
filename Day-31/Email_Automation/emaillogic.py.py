'''
import smtplib
import os
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

#https://myaccount.google.com/apppasswords

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "sameernawab66gmail.com"
SENDER_PASSWORD = "tena qrsr eclb umnk"



def send_email(to_email, subject, body, attachments=None):
    try:
        msg = MIMEMultipart()
        msg["From"] = SENDER_EMAIL
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        if attachments:
            for file_path in attachments:
                if os.path.exits(file_path):
                    with open(file_path, "rb") as f:
                        mime_base = MIMEBase("application","octet-stream")
                        mime_base.set_payload(f.read())
                        encoders.encode_base64(mime_base)
                        mime_base.add_header("Content-Disposition",
                            f" attachemts; filename={os.path.basename}(file_path) ")
                        
                            
                        
                        msg.attach(mime_base)
                else:
                        print(f"File '{file_path}' not found. Skipping...")
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, to_email, msg.as_string())
        server.quit()

        print(f"Email sent to {to_email}")


    except Exception as e:
        print(f"Error sending email to {to_email}: {e}")


def send_bulk_emails(csv_file, subject, body, attachments=None):
    try:
        csv_path = os.path.abspath(csv_file)
        if not os.path.exists(csv_path):
            print(f"Error: CSV file '{csv_file}' not found.")
            return
        with open(csv_path, newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    email = row[0]
                    send_email(email, subject, body, attachments)


    except Exception as e:
        print(f"Error reading CSV file: {e}")

'''

import smtplib
import os
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders



# Gmail SMTP Details
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# Your Gmail
SENDER_EMAIL = "sameernawab66@gmail.com"

# Gmail App Password
SENDER_PASSWORD = "tena qrsr eclb umnk"


# Function to send single email
def send_email(to_email, subject, body, attachments=None):

    try:
        msg = MIMEMultipart()

        msg["From"] = SENDER_EMAIL
        msg["To"] = to_email
        msg["Subject"] = subject

        # Email body
        msg.attach(MIMEText(body, "plain"))

        # Attachments
        if attachments:

            for file_path in attachments:

                if os.path.exists(file_path):

                    with open(file_path, "rb") as f:

                        mime_base = MIMEBase("application", "octet-stream")

                        mime_base.set_payload(f.read())

                        encoders.encode_base64(mime_base)

                        mime_base.add_header(
                            "Content-Disposition",
                            f'attachment; filename="{os.path.basename(file_path)}"'
                        )

                        msg.attach(mime_base)

                else:
                    print(f"File '{file_path}' not found. Skipping...")

        # SMTP Connection
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)

        server.starttls()

        server.login(SENDER_EMAIL, SENDER_PASSWORD)

        server.sendmail(SENDER_EMAIL, to_email, msg.as_string())

        server.quit()

        print(f"Email sent successfully to {to_email}")

    except Exception as e:
        print(f"Error sending email to {to_email}: {e}")


# Function to send bulk emails
def send_bulk_emails(csv_file, subject, body, attachments=None):

    try:
        csv_path = os.path.abspath(csv_file)

        if not os.path.exists(csv_path):
            print("CSV file not found.")
            return

        with open(csv_path, "r", newline="", encoding="utf-8") as file:

            reader = csv.reader(file)

            for row in reader:

                if row:
                    recipient = row[0]

                    send_email(recipient, subject, body, attachments)

    except Exception as e:
        print(f"Error reading CSV file: {e}")





































    
