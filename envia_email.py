#!/usr/bin/python
#-=- encoding: utf-8 -=-

# LIBS
import os
import commands
import time
import smtplib
from email.MIMEText import MIMEText

# FUNCAO ENVIA EMAIL
def envia_email(recebe1,recebe2):
    # Defina as variaveis da conta de email.
    SMTP    =   "smtp.dominio.com.br"
    PORTA   =   "26"
    LOGIN   =   "conta@dominio.com.br"
    EMAIL   =   "ti@dominio.com.br"
    PASS    =   "senha-email"
    if (PORTA == 465):
        SMTPSERVER = smtplib.SMTP_SSL
        PORTA = str(PORTA)
        ASSUNTO="Dump Mysql - Prod"
        HOSTNAME = commands.getoutput("hostname")
        MENSAGEM="Servidor: %s \n %s" %(HOSTNAME,recebe2)
        FROM=EMAIL
        TO=recebe1
        serv=SMTPSERVER()
        serv.connect(SMTP,PORTA)
        serv.login(LOGIN,PASS)
        msg1 = MIMEText("%s"% MENSAGEM,"html")
        msg1['Subject']=(ASSUNTO)
        msg1['From']=FROM
        msg1['To']=TO
        msg1['Content-type']="text/html"
        serv.sendmail(FROM,TO, msg1.as_string())
        serv.quit()
    else:
        SMTPSERVER = smtplib.SMTP
        PORTA = str(PORTA)
        ASSUNTO="Dump Mysql - Prod"
        HOSTNAME = commands.getoutput("hostname")
        MENSAGEM="Servidor: %s \n %s" %(HOSTNAME,recebe2)
        FROM=EMAIL
        TO=recebe1
        serv=SMTPSERVER()
        serv.connect(SMTP,PORTA)
        serv.starttls()
        serv.login(LOGIN,PASS)
        msg1 = MIMEText("%s"% MENSAGEM,"html")
        msg1['Subject']=(ASSUNTO)
        msg1['From']=FROM
        msg1['To']=TO
        msg1['Content-type']="text/html"
        serv.sendmail(FROM,TO, msg1.as_string())
        serv.quit()
  
