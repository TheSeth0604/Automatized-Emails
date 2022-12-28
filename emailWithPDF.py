import csv 
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

email_user= 'alvarocrispin0604@gmail.com'
password="vfzzadiibbplfrqr"
subject="Email Example"

with open('emails.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    for line in csv_reader:
        text="hello " + line[1] + " this is a example email"
        
        #print(text)
        email_send=line[0]
        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = email_send
        msg['Subject'] = subject
        msg.attach(MIMEText(text,"plain"))
        text = msg.as_string()
        
        pdfname = line[1]+'.pdf'
        binary_pdf = open(pdfname, 'rb')
        payload = MIMEBase('application', 'octate-stream', Name=pdfname)
        payload.set_payload((binary_pdf).read())
        encoders.encode_base64(payload)
        payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
        msg.attach(payload)

        #use gmail with port
        session = smtplib.SMTP('smtp.gmail.com', 587)
        
        #enable security
        session.starttls()
        
        #login with mail_id and password
        session.login(email_user, password)
        
        text = msg.as_string()
        session.sendmail(email_user, email_send, text)
        session.quit()
        print('Mail Sent')
        
        