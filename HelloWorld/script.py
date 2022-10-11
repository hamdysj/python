#Scripts - Writing program to automate a task

import os
import time
import smtplib

def cur_directory():
    cwd = os.getcwd() #cwd - Current Write Directory
    print(cwd)

def file_path(filename):
    path = os.path.abspath(filename)
    print(path)

#SMTP Module
smtObj = smtplib.SMTP('smtp.gmail.com', 587) #Parameters(DomainName, PortNumber) Port 587 is used because we are using TLS connection
smtObj.ehlo()
smtObj.starttls()
smtObj.login()



t = time.time() #returns seconds
docs = 'newtext.txt'
print(time.ctime(t))
cur_directory()
file_path(docs)