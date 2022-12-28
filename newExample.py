#importar librerias necesarias
import smtplib, ssl, csv
from email.message import EmailMessage

#usuario del que enviara
sender = 'alvarocrispin0604@gmail.com'
password = 'vfzzadiibbplfrqr'

#contexto del email
subject = 'Email Example' #titulo
body_message = 'Hola' #type message

#conexion con el servidor
context = ssl.create_default_context()
server = smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context)

server.login(sender,password)

#formula para enviar emails
with open('emails.csv', 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        em = EmailMessage()
        em['From'] = sender
        em['To'] = row
        em['Subject'] = subject
        em.set_content(body_message)
        server.send_message(em)
        print("The message sent")