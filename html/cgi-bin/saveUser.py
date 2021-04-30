#!/usr/bin/env python3
# coding: utf-8





import mysql.connector
import json
import cgi
import webbrowser
from mysql.connector.errors import Error
import flask 

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



def saveUser(dbconnection):
	try:
		form = cgi.FieldStorage()
		name = form.getvalue("name")
		username = form.getvalue("usernamesignup")
		password = form.getvalue("pwsignup")
		passwordcheck = form.getvalue("pwdsignupconfirm")
		if password != passwordcheck:
			print('Content-Type: text/html\n')
			redirect = "http://localhost:8000/error.html"
			print('<html>')
			print('  <head>')
			print('    <meta http-equiv="refresh" content="0;url='+str(redirect)+'" />') 
			print('  </head>')
			print('</html>')
			exit(1)
		mycursor = dbconnection.cursor()
		sql = 'INSERT INTO Users (Username, Pass, Name) VALUES (%s,%s,%s)'
		vals = (username, password, name)
		mycursor.execute(sql,vals)
		dbconnection.commit()
		return
	except mysql.connector.Error as err:
		if str(Error(errno=1062)):
			print('Content-Type: text/html\n')
			redirect = "http://localhost:8000/userexists.html"
			print('<html>')
			print('  <head>')
			print('    <meta http-equiv="refresh" content="0;url='+str(redirect)+'" />') 
			print('  </head>')
			print('</html>')
			exit(1)
		raise



if __name__=="__main__":
	try:
		dbconnection = connectToDb(host="localhost",user="sy306",password="sy306",database="projectdb")
		saveUser(dbconnection)
		#webbrowser.open("localhost:8000/userconfirmation.html")
		print('Content-Type: text/html\n')
		redirect = "http://localhost:8000/userconfirmation.html"
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
