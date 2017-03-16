#!/usr/bin/python
#-=- encoding: utf-8 -=-

# libs
import os
import commands
import time
import smtplib
from email.MIMEText import MIMEText

# function email
def send_email(receive1,receive2):
	# variables
    	SMTP    =   "smtp.gmail.com"
    	port   =   "587"
    	login   =   "login@gmail.com"
    	email   =   "login"
    	PASS    =   "password"
	# email
  	SMTPSERVER = smtplib.SMTP
        port = str(port)
        ASSUNTO="Dump Mysql - Prod"
        HOSTNAME = commands.getoutput("hostname")
        MENSAGEM="Servidor: %s \n %s" %(HOSTNAME,receive2)
        FROM=email
        TO=receive1
        serv=SMTPSERVER()
        serv.connect(SMTP,port)
        serv.starttls()
        serv.login(login,PASS)
        msg1 = MIMEText("%s"% MENSAGEM,"html")
        msg1['Subject']=(ASSUNTO)
        msg1['From']=FROM
        msg1['To']=TO
        msg1['Content-type']="text/html"
        serv.sendmail(FROM,TO, msg1.as_string())
        serv.quit()
  
# execute function
#send_email("vandocouto@gmail.com", "teste")

