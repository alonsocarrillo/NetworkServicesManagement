import smtplib
from email.message import EmailMessage
from path import *
import imghdr

COMMASPACE = ', '
# Define params
# Nueva cuenta de GMAIL
# dummycuentaredes@gmail.com
# "Secreto123"

mailsender = "dummycuentaredes@gmail.com"
mailreceip = "dummycuentaredes@gmail.com"
mailserver = 'smtp.gmail.com: 587'
password = 'Secreto123'

def send_alert_attached(subject,file_name):
    """ Will send e-mail, attaching png
    files in the flist.
    """
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = mailsender
    msg['To'] = mailreceip
    msg.set_content("This is PDF try")
    file = open(pngpath+"prueba.pdf", "rb")
    file_data = file.read()

    msg.add_attachment(file_data, maintype="application", subtype="octet-stream",filename=file_name)

    mserver = smtplib.SMTP(mailserver) # con esto se hace el envio al servidor de GMAIL
    mserver.starttls()
    # Login Credentials for sending the mail
    mserver.login(mailsender, password)

    mserver.sendmail(mailsender, mailreceip, msg.as_string())
    mserver.quit()