"""Email support for 未来Mail"""


import os
import smtplib
from dotenv import load_dotenv
from functools import lru_cache
from email.header import Header
from email.utils import formataddr
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


@lru_cache()  # To cache the data
def mail_cred():
    load_dotenv()  # Loads .env file to access Environment_Variables


mail_cred()  # Call the above function to load the environment variables

mail_address = os.environ.get("EMAIL_ADDRESS")  # Load mail address from Environment_variables
password = os.environ.get("EMAIL_PASSWORD")  # Load Email_password from Environment_Variables...



def send_mail(receiver_mail, _text, subject):  # used to send the email
    # message = EmailMessage()
    message = MIMEMultipart('alternative')
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

        html = f"""<!DOCTYPE HTML PUBLIC "-//W3C//DTD XHTML 1.0 Transitional //EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="x-apple-disable-message-reformatting">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <title></title>
  
<link href="https://fonts.googleapis.com/css?family=Lobster+Two:400,700&display=swap" rel="stylesheet" type="text/css">
</head>

<body class="clean-body" style="margin: 0;padding: 0;-webkit-text-size-adjust: 100%;background-color: #ecf9f2">
  <table style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;min-width: 320px;Margin: 0 auto;background-color: #ecf9f2;width:100%" cellpadding="0" cellspacing="0">
  <tbody>
  <tr style="vertical-align: top">
    <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">
<div class="u-row-container" style="padding: 0px;background-color: transparent">
  <div class="u-row" style="Margin: 0 auto;min-width: 320px;max-width: 500px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;">
    <div style="border-collapse: collapse;display: table;width: 100%;background-color: transparent;">
     
<div class="u-col u-col-100" style="max-width: 320px;min-width: 500px;display: table-cell;vertical-align: top;">
  <div style="width: 100% !important;">
  <!--[if (!mso)&(!IE)]><!--><div style="padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;"><!--<![endif]-->
  
<table style="font-family:'Lobster Two',cursive;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
  <tbody>
    <tr>
      <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:'Lobster Two',cursive;" align="left">
        
<table width="100%" cellpadding="0" cellspacing="0" border="0">
  <tr>
    <td style="padding-right: 0px;padding-left: 0px;" align="center">
      <img align="center" border="0" src="https://s3.amazonaws.com/unroll-images-production/projects%2F0%2F1619377698756-86599" alt="Image" title="Image" style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: inline-block !important;border: none;height: auto;float: none;width: 24%;max-width: 115.2px;" width="115.2"/>
      
    </td>
  </tr>
</table>
      </td>
    </tr>
  </tbody>
</table>

<table style="font-family:'Lobster Two',cursive;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
  <tbody>
    <tr>
      <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:'Lobster Two',cursive;" align="left">
        
  <table height="0px" align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;border-top: 2px dashed #b1d4e0;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
    <tbody>
      <tr style="vertical-align: top">
        <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;font-size: 0px;line-height: 0px;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
          <span>&#160;</span>
        </td>
      </tr>
    </tbody>
  </table>
      </td>
    </tr>
  </tbody>
</table>
  </div>
  </div>
</div>
    </div>
  </div>
</div>
<div class="u-row-container" style="padding: 0px;background-color: transparent">
  <div class="u-row" style="Margin: 0 auto;min-width: 320px;max-width: 500px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;">
    <div style="border-collapse: collapse;display: table;width: 100%;background-color: transparent;">
      
<div class="u-col u-col-100" style="max-width: 320px;min-width: 500px;display: table-cell;vertical-align: top;">
  <div style="background-color: #ebeef1;width: 100% !important;">
  <!--[if (!mso)&(!IE)]><!--><div style="padding: 0px;border-top: 2px dashed #b1d4e0;border-left: 2px dashed #b1d4e0;border-right: 2px dashed #b1d4e0;border-bottom: 2px dashed #b1d4e0;"><!--<![endif]-->
  
<table style="font-family:'Lobster Two',cursive;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
  <tbody>
    <tr>
      <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:'Lobster Two',cursive;" align="left">
  <div style="color: #000000; line-height: 140%; text-align: left; word-wrap: break-word;">
    <p style="font-size: 14px; line-height: 140%;">{_text}</p>
  </div>
      </td>
    </tr>
  </tbody>
</table>
  </div>
  </div>
</div>
    </div>
  </div>
</div>
<div class="u-row-container" style="padding: 0px;background-color: transparent">
  <div class="u-row" style="Margin: 0 auto;min-width: 320px;max-width: 500px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;">
    <div style="border-collapse: collapse;display: table;width: 100%;background-color: transparent;">
      
<div class="u-col u-col-100" style="max-width: 320px;min-width: 500px;display: table-cell;vertical-align: top;">
  <div style="width: 100% !important;">
  <div style="padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;">
  
<table style="font-family:'Lobster Two',cursive;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
  <tbody>
    <tr>
      <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:'Lobster Two',cursive;" align="left">
        
  <table height="0px" align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;border-top: 1px solid #b1d4e0;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
    <tbody>
      <tr style="vertical-align: top">
        <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;font-size: 0px;line-height: 0px;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
          <span>&#160;</span>
        </td>
      </tr>
    </tbody>
  </table>

      </td>
    </tr>
  </tbody>
</table>

<table style="font-family:'Lobster Two',cursive;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
  <tbody>
    <tr>
      <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:'Lobster Two',cursive;" align="left">
        
<div align="center">
    <a href="https://miraimail.herokuapp.com/" target="_blank" style="box-sizing: border-box;display: inline-block;font-family:'Lobster Two',cursive;text-decoration: none;-webkit-text-size-adjust: none;text-align: center;color: #FFFFFF; background-color: #2e8bc0; border-radius: 4px; -webkit-border-radius: 4px; -moz-border-radius: 4px; width:auto; max-width:100%; overflow-wrap: break-word; word-break: break-word; word-wrap:break-word; mso-border-alt: none;">
      <span style="display:block;padding:10px 20px;line-height:120%;"><span style="font-size: 14px; line-height: 16.8px;">未来Mail</span></span>
    </a>
 
</div>
      </td>
    </tr>
  </tbody>
</table>

  </div>
  </div>
</div>
    </div>
  </div>
</div>
    </td>
  </tr>
  </tbody>
  </table>
</body>
</html>
"""
        # part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')
        # message.set_content(_text)  # Message i.e body of the mail
        # message.attach(part1)
        message.attach(part2)

        smtp.send_message(message)