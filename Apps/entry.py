import pymysql
import mysql.connector

# global con, cur,

mypass = "Root123!!!"
mydatabase = "nlidb"
con_db = mysql.connector.connect(host="localhost", user="root", password=mypass, database=mydatabase)
cur_db = con_db.cursor()

'''mypass = "Root123!!!"
mydatabase="librarymanagement"
con = pymysql.connect (host="localhost", user="root", password=mypass, database=mydatabase)
cur = con.cursor() 
'''




