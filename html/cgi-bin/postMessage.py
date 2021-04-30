#!/usr/bin/env python3
# coding: utf-8


import mysql.connector
import json
import cgi
import webbrowser
from mysql.connector.errors import Error
import os 

def getCookies():
    if 'HTTP_COOKIE' in os.environ:
         cookie_string = os.environ.get('HTTP_COOKIE')
         parseCookie = cookie_string.strip('User=')
         parseCookie = parseCookie.split(';')
         return(parseCookie[1])


def connectToDb(host,user,password,database):
	try:
		mydb = mysql.connector.connect(
			host=host,
			user=user,
			password=password,
			database=database)
		return(mydb)
	except mysql.connector.Error as err:
		print("connedtToDb: unable to connect to database check parameters")
		raise



def postMessage(dbconnection):
	try:
		form = cgi.FieldStorage()
		message = form.getvalue("message")
		username = getCookies()
		username = username.split("User=")
		username = username[1]
		print(username)
		mycursor = dbconnection.cursor()
		sql = 'INSERT INTO Messages (Username, Message) VALUES ((SELECT Username FROM Users WHERE Username =%s),%s)'
		vals = (username, message)
		mycursor.execute(sql,vals)
		dbconnection.commit()
		return
	except mysql.connector.Error as err:
		if str(Error(errno=1062)):
			print(err)
		raise



if __name__=="__main__":
	try:
		dbconnection = connectToDb(host="localhost",user="sy306",password="sy306",database="projectdb")
		postMessage(dbconnection)
		#webbrowser.open("localhost:8000/userconfirmation.html")
		print('Content-Type: text/html\n')
		redirect = "http://localhost:8000/MembersOnlyMessageBoard.html"
		print('<html>')
		print('  <head>')
		print('    <meta http-equiv="refresh" content="0;url='+str(redirect)+'" />') 
		print('  </head>')
		print('</html>')
		exit(0)
	except Exception as ex:
		print("Content-Type: text/html\n")		
		print(ex)
		exit(1)
