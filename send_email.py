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
    	login   =   "monitorcntlog@gmail.com"
    	email   =   "monitorcntlog"
    	PASS    =   "cnt@2019"
	# email
  	SMTPSERVER = smtplib.SMTP
        port = str(port)
        SUBJECT="Dump Mysql - Prod"
        HOSTNAME = commands.getoutput("hostname")
        MESSAGE="Servidor: %s \n %s" %(HOSTNAME,receive2)
        FROM=email
        recipients = [receive1, 'vandocouto@gmail.com']
        #TO=receive1
        serv=SMTPSERVER()
        serv.connect(SMTP,port)
        serv.starttls()
        serv.login(login,PASS)
        msg1 = MIMEText("%s"% MESSAGE,"html")
        msg1['Subject']=(SUBJECT)
        msg1['From']=FROM
        msg1['To']= ", ".join(recipients)
        msg1['Content-type']="text/html"
        serv.sendmail(FROM,recipients, msg1.as_string())
        serv.quit()
  
# execute function
# send_email("vandocouto@gmail.com,tecnologia@cntlog.com.br", "cntlog")

