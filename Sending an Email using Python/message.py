# Author: Akrash Sharma

from email.mime.multipart import MIMEMultipart  # MIME stands for Multi-Purpose Internet Mail Extensions
from email.mime.text import MIMEText  # MIME defines the format for emails
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib

# the email library has many templates and I am using a html template for the body text
template = Template(Path("template.html").read_text())  # this returns the text in the html file as a string
message = MIMEMultipart()
message["from"] = "your email address"  # type your email address here
message["to"] = "receiver's email address"    # type the receiver's email address here
message["subject"] = "Message from Python"  # type your subject line here
body = template.substitute({"receiver_name": "", "my_name": ""})  # fill in the empty strings appropriately
message.attach(MIMEText(body, "html"))
message.attach(MIMEImage(Path("image4.bmp").read_bytes()))  # read_bytes returns the image data in binary


with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:  # connect with Google's servers
    smtp.ehlo()  # think of this as a greeting to the server from the client
    smtp.starttls()  # this puts the smtp connection in tls (transport layer security) mode
    smtp.login("your email address", "your password")  # type your email address and password to login
    smtp.send_message(message)
