'''
SMTP Email:
- gmail: smtp.gmail.com
- hotmail: smtp.live.com
- outlook: outlook.office365.com
- yahoo: smtp.mail.yahoo.com

Enable less secure apps
Try to go through gmail captcha
Add a port number by changing code to 
    smptplib.SMTP('smtp.gmail.com',port = 587)
'''

# Simple Mail Transfer Protocol: rules how emails are sent and passed around in the internet
# Mail Servers: Post Office, Recipient: Mailbox, SMTP: Postman

import smtplib

email = 'email'
password = 'password'
# Create connection
with smtplib.SMTP('smtp.gmail.com') as connection:
    # Encrypt Message
    connection.starttls()
    # login
    connection.login(user=email, password = password)
    # Add subject -> less chance to be spam
    connection.sendmail(from_addr=email, to_addrs=email, msg = "Subject:Hello there\n\nThis is a test email")
# we can also use with

