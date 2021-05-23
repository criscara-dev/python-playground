import smtplib
from email.message import EmailMessage
# 2 liobraries to 
from string import Template
from pathlib import Path # or os.path

html = Template(Path('./index.html').read_text())

email= EmailMessage()
email[ 'from' ] = 'Cris Cara'
email['to' ] = 'c.caratti@me.com'
email[ 'subject'] = 'test from Mac'
# email.set_content('I am a Python Master!')
email.set_content(html.substitute({'client':'John','name':'Cris','description':'I am a Python Master!'}),'html')

with smtplib.SMTP( host='smtp.gmail.com',port=587) as smtp:
        smtp.ehlo() # handshake the server
        smtp.starttls() # start encryption
        smtp.login('cristian.caratti.xx@gmail.com','<password>') # log in the Gmail account
        smtp.send_message(email)
        print('all good!')    
