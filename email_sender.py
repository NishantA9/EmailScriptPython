import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get email credentials from environment variables
EMAIL_USER = os.getenv('EMAIL_USER')
EMAIL_PASS = os.getenv('EMAIL_PASS')

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'CherryFire'
email['to'] = 'nsa123@gustr.com'
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_USER, EMAIL_PASS)
    smtp.send_message(email)
    print('all good boss!')
    
#run this code in terminal








