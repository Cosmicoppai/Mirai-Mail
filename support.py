"""Email support for 未来Mail"""


import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
from functools import lru_cache
from email.header import Header
from email.utils import formataddr


@lru_cache()  # To cache the data
def mail_cred():
    load_dotenv()  # Loads .env file to access Environment_Variables


mail_cred()  # Call the above function to load the environment variables

mail_address = os.environ.get("EMAIL_ADDRESS")  # Load mail address from Environment_variables
password = os.environ.get("EMAIL_PASSWORD")  # Load Email_password from Environment_Variables...



def send_mail(receiver_mail, _text, subject):  # used to send the email
    message = EmailMessage()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:  # Gmail compatible smtp and port address

        smtp.login(mail_address, password)

        # Below documented lines are needed if you're sending via non ssl port/method
        """smtp.ehlo()  # To identify ourselves as encrypted connection
        smtp.starttls()  # To re-identify ourselves as encrypted connection
        smtp.login(mail_address, password)
        subject = "Test ..."
        body = "is it working ?..."

        msg = f"{subject}\n\n{body}"""


        message['Subject'] = subject
        message['From'] = formataddr((str(Header('未来Mail', 'utf-8')), mail_address))
        message['To'] = receiver_mail
        message.set_content(_text)  # Message i.e body of the mail

        smtp.send_message(message)


# send_mail()
# print("Successful \n hahahahaha")