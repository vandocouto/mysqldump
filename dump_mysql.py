#!/usr/bin/python
#-=- encoding: utf-8 -=-

import MySQLdb
import os
import shutil
import commands
import datetime
from send_email import send_email

# variables mysql
host = '127.0.0.1'
user = 'root'
password = ''
path = '/opt/backup/MYSQL_dump'
bar = '/'
tpoint = ":"
email= "tecnologia@cntlog.com.br"
bucket = "mysqldumpcntlog"

# retention
days_ago = 5

# check if existing is directory
if os.path.exists(path):
    log = 'directory existing'
else:
    os.mkdir(path) 
    
now  = datetime.datetime.now()  
today = now.strftime('%d-%m')
schedule = str(now.hour) + tpoint + str(now.minute) 

# check if existiong is directory date 
if os.path.exists(path + bar + today):
    log = 'directory existing'
else:
    os.mkdir(path + bar + today)

# create directory + directory start dump
dir_date = (path + bar + today + bar + schedule)
os.mkdir(dir_date)

# Connecting to mysql
# password
#db = MySQLdb.connect(host, user, password)
# not password
db = MySQLdb.connect()
cursor = db.cursor()
cursor.execute("show databases")
databases = cursor.fetchall()

# start dump
table = '<table class="border" align="center" valign="top" width="800">'
messages = table
for base in databases:
        hour = commands.getoutput("date +'%r'")
	try:
        	if base[0] != 'information_schema' and base[0] != 'performance_schema':
                	print base[0]
			# not password
                	if os.system('mysqldump -x -e %s | gzip > %s/%s.sql.gz' %(base[0],dir_date,base[0])) == 0:
                   		messages += "<tr><td>%s</td><td>%s</td><td><b style='color:green'>OK</b></td></tr>" %(hour,base[0])
                	else:
                     		messages += "<tr><td>%s</td><td>%s</td><td><b style='color:red'>NOT</b></td></tr>" %(hour,base[0])
	except:
    		continue
messages += "</table>"
print messages

# remove directory old
now = datetime.date.today()
dateold = (now - datetime.timedelta(days_ago)).strftime('%d-%m')
if os.path.exists(path + bar + dateold):
    shutil.rmtree(path + bar + dateold)

# aws s3
dir_date = (path)
os.system('aws s3 sync %s s3://%s' %(dir_date,bucket))
os.system('aws s3 rm s3://%s/%s --recursive' %(bucket,dateold)) 

# function email
send_email(email,messages)

