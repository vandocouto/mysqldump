MySQL Dump 
==========

- MySQL Backup and Report by Email
- The backups are generated local and copied to the S3
- Configure awscli * * *

### dump_mysql.py
<pre>
# variables mysql
host 		= IP'
user 		= 'user'
password 	= 'password'
path 		= '/MYSQL_dump'
email		= "email@domain.com"
bucket 		= "your-bucket"
</pre>

### send_email.py
<pre>
# variables
SMTP    =   "smtp.gmail.com"
port   	=   "587"
login   =   "login@gmail.com"
email   =   "login"
PASS    =   "password"
</pre>
