#!/usr/bin/python
#-=- encoding: utf-8 -=-

import MySQLdb
import os
import shutil
import commands
import datetime
from envia_email import envia_email

#INSIRA AQUI OS DADOS DO SERVIDOR MYSQL 
HOST = '127.0.0.1'
USER = 'root'
PASSWORD = 'senha-banco'
PATH = '/MYSQL_DUMP'
BARRA = '/'
DOIS_PONTOS = ":"
EMAIL= "email@dominio.com.br"

#DEFINA A VARIAVEL PARA APAGAR O BKP'S ANTIGOS APÓS:
DIAS_ATRAS = 3

#Verifica se existe o diretório de armazenamento dos Dump's.
if os.path.exists(PATH):
    log = 'Dir ja existe'
else:
    os.mkdir(PATH) 
    
NOW  = datetime.datetime.now()  
HOJE = NOW.strftime('%d-%m')
HORARIO_ATUAL = str(NOW.hour) + DOIS_PONTOS + str(NOW.minute) 

#Verificar se existe o diretório do dia atual.
if os.path.exists(PATH + BARRA + HOJE):
    log = 'Dir ja existe'
else:
    os.mkdir(PATH + BARRA + HOJE)

#Cria o diretório com a hora início do Dump.
DIR_HORAIO = (PATH + BARRA + HOJE + BARRA + HORARIO_ATUAL)
os.mkdir(DIR_HORAIO)

# Data.
DATA = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
INICIO = DATA + ' Started dump backup'

#Log _dump início e fim
DUMP = "_dump"
var_file = open(DIR_HORAIO + BARRA + DUMP, "a")
var_file.write(INICIO + "\n")

#Conectando no MySQL.
db = MySQLdb.connect(HOST, USER, PASSWORD)
cursor = db.cursor()
cursor.execute("show databases")
databases = cursor.fetchall()

#Início do Dump.
TABELA = '<table class="border" align="center" valign="top" width="800">'
messages = TABELA
for base in databases:
	DIR_HORARIO = (PATH + BARRA + HOJE + BARRA + HORARIO_ATUAL +BARRA + base[0])
	os.mkdir(DIR_HORARIO)
        HORARIO = commands.getoutput("date +'%r'")
	try:
        	if base[0] != 'information_schema' and base[0] != 'performance_schema':
                	print base[0]
			cursor.execute('use %s' %base[0]) 
			cursor.execute('show tables')
			tables = cursor.fetchall()
			for i in tables:
				if str(i[0]) != 'event': 
        				DESTINO = DIR_HORAIO + BARRA + base[0] + BARRA + i[0]+'.sql.gz'
                			if os.system('/usr/bin/mysqldump -h %s -u %s -p%s -x -e %s %s | gzip > %s' %(HOST,USER,PASSWORD,base[0],i[0],DESTINO)) == 0:
                   				messages += "<tr><td>%s</td><td>%s</td><td>%s</td><td><b style='color:green'>OK</b></td></tr>" \
                      				%(HORARIO,base[0],i[0])
                			else:
                       				messages += "<tr><td>%s</td><td>%s</td><td>%s</td><td><b style='color:red'>NOT</b></td></tr>" \
                       				%(HORARIO,base[0],i[0])
	except:
    		continue
		
messages += "</table>"
		
print messages

#Removendo Dump's anteriores.
AGORA = datetime.date.today()
DATAANTIGA = (AGORA - datetime.timedelta(DIAS_ATRAS)).strftime('%d-%m')
if os.path.exists(PATH + BARRA + DATAANTIGA):
    shutil.rmtree(PATH + BARRA + DATAANTIGA)

#Data e arquivo de log.
DATA = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
FIM = DATA + ' Finish dump backup'
DUMP = "_dump"
var_file = open(DIR_HORAIO + BARRA + DUMP, "a")
var_file.write(FIM + "\n")

#Função envia email.
envia_email(EMAIL,messages)

