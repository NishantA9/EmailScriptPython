# Email Sender with Python's `smtplib`

This project demonstrates how to send an HTML email using Python's `smtplib` library. The email content is read from an HTML file and sent to a specified recipient.

## Prerequisites

Ensure you have the following installed:
- Python 3.x

## Project Structure

.
├── send_email.py
├── index.html
└── README.md

- `send_email.py`: The main script for sending the email.
- `index.html`: The HTML template used for the email content.
- `README.md`: Project documentation.

## Setup

1. **Clone the repository** (if applicable) or download the project files to your local machine.

2. **Create an HTML template** named `index.html` in the project directory. (I have provided the HTML file)

## Generate an App Password for your Gmail account:

Go to your Google Account settings.
Select 'Security' and enable '2-Step Verification'.
Go to 'App passwords', select 'Mail' as the app and 'Other' as the device.
Copy the generated app password.


##  Usage
Update the send_email.py script with your Gmail credentials and the recipient's email address.

## Run the script:

python send_email.py

##  Notes
Replace the email address and app-specific password with your own.
Ensure that 'Less secure app access' is enabled in your Gmail account if you encounter issues.

## References (search on google (sorry in advance))
smtplib Documentation
EmailMessage Documentation
Gmail App Passwords


##  Made by Nishant Acharekar, under Course of Complete Python Developer 2024 by ZTM on Udemy