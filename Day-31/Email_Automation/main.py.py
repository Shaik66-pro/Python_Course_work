'''
from  emaillogic import *

subject = input ("Enter the email subject : ")
body = input("Enter email body : ")


choice = input(Do You Want To Send
                    (1) Single Email or
                    (2) Bulk Emails? Enter 1 or 2: )
attach_choice = input("Do You Want To Add attachments? (Y/N): ").lower()
attachments = []


if attach_choice == "y":
    files = input("Enter file path separated by commas: ").split(',')
    attachments = [f.strip() for f in files]
if choice == "1":
    recipient = input("Enter the recipient email: ")
    send_email(recipient, subject, body, attachments)
elif choice == '2':
    csv_file = input("Enter path to CSV file with email addresses : ")
    send_bulk_emails(csv_file, subject, body, attachments)
else:
        print("Invaild Choice! Please Enter the 1 or 2.")

'''
        
from emaillogic import*

subject = input("Enter the email subject: ")
body = input("Enter email body: ")

choice = input('''
Do You Want To Send
(1) Single Email or
(2) Bulk Emails?

Enter 1 or 2: ''').strip()

attach_choice = input("Do You Want To Add Attachments? (Y/N): ").lower().strip()

attachments = []

if attach_choice == "y":
    files = input("Enter file paths separated by commas: ").split(',')
    attachments = [f.strip() for f in files]

if choice == "1":
    recipient = input("Enter the recipient email: ")
    send_email(recipient, subject, body, attachments)

elif choice == "2":
    csv_file = input("Enter path to CSV file with email addresses: ")
    send_bulk_emails(csv_file, subject, body, attachments)

else:
    print("Invalid Choice! Please enter 1 or 2.")
