#!/usr/bin/env python3
# coding: utf-8

import mysql.connector
import json
import cgi
import webbrowser
from http import cookies


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



def checkLogin(dbconnection):
	try:
		form = cgi.FieldStorage()
		username = form.getvalue("username")
		password = form.getvalue("password")
		mycursor = dbconnection.cursor()
		sql = 'SELECT * FROM Users WHERE (Username = "%s" AND Pass = "%s")'%(username,password)
		#vals = (username, password)
		mycursor.execute(sql)
		result = mycursor.fetchone()
		if result == None:
			print('Content-Type: text/html\n')
			redirect = "http://localhost:8000/error.html"
			print('<html>')
			print('  <head>')
			print('    <meta http-equiv="refresh" content="0;url='+str(redirect)+'" />') 
			print('  </head>')
			print('</html>')
			exit(1)
		elif result[0] == username and result[1] == password:
			cookie = cookies.SimpleCookie()
			cookie["User"] = username
			cookie["LoggedIn"] = 'True'
			cookie["User"]['expires'] = 'Session'
			cookie["LoggedIn"]['expires'] = 'Session'
			cookie['User']['path'] = '/'
			cookie['LoggedIn']['path'] = '/'
			cookie['UserType'] = result[2]
			cookie['UserType']['expires'] = 'Session'
			cookie['UserType']['path'] = '/'
			print(cookie)
			print('Content-Type: text/html\n')
			redirect = "http://localhost:8000/MembersOnlyMessageBoard.html"
			print('<html>')
			print('  <head>')
			print('    <meta http-equiv="refresh" content="0;url='+str(redirect)+'" />') 
			print('  </head>')
			print('</html>')
			exit(0)
		else:
			print('Content-Type: text/html\n')
			redirect = "http://localhost:8000/error.html"
			print('<html>')
			print('  <head>')
			print('    <meta http-equiv="refresh" content="0;url='+str(redirect)+'" />') 
			print('  </head>')
			print('</html>')
			exit(1)
	except mysql.connector.Error as err:
		print("Content-Type: text/html\n")
		print('Unable to perform query')
		raise



if __name__=="__main__":
	try:
		dbconnection = connectToDb(host="localhost",user="sy306",password="sy306",database="projectdb")
		checkLogin(dbconnection)
		print("Content-Type: text/html\n")
		print("Test!")
	except Exception as ex:
		print("Content-Type: text/html\n")		
		print(ex)
		exit(1)
