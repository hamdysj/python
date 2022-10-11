import smtplib

#SMTP Module
#Parameters(DomainName, PortNumber) Port 587 is used because we are using TLS connection

smtObj = smtplib.SMTP('smtp.gmail.com', 587)
smtObj.ehlo()
smtObj.starttls()
smtObj.login("hamdysj@gmail.com","Input Password") #Password in Notes
sender = 'hamdysj@gmail.com'
receiver = 'hfsulaimon@gmail.com'
msg = '''\
Subject: Python SMTP Email Generation.


This is Awesome from the stable of python Programming!!!!

'''
smtObj.sendmail(sender,receiver,msg)
smtObj.quit()
