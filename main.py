import csv 
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

email_user= ''
password=""
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
        
        server = smtplib.SMTP_SSL("smtp.gmail.com",465)
        server.login(email_user,password)
        server.sendmail(email_user,email_send,text)
        
        server.quit() 
        
