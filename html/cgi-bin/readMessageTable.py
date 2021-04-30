#!/usr/bin/env python3
# coding: utf-8

# In[1]:


#!/usr/bin/env python3

import mysql.connector
import json


# In[9]:


def connectToDb(host, user, password, database):
    '''
    Effects: Connects to the database and returns a connector otherwise throw an exception
    Required Parameters:
        host: host address
        user: database user
        password: password for the user
        database: the intended database to connect to
    '''
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


# In[10]:


def selectMessages(dbconnection, table):
    '''
    Effects: Selects all items from a passed table 
    Returns: tupple that represents all of the data in the table
    '''
    try:
        mycursor = dbconnection.cursor()
        selectQuery = 'SELECT * FROM %s'%(table)
        mycursor.execute(selectQuery)
        return(mycursor.fetchall())
    except mysql.connector.Error as err:
        print('selectProducts: Unable to preform query check your parameters')
        raise


# In[25]:


def sendToWebClient(resultData):
    #print('1. itterate through the entire result data collection')
    totalList = [] 
    #print('1a. access each of the tupples')
    for i in range(len(resultData)):
        user,message,time = resultData[i]
        #print('2. create a dictionary')
        myDictionary = {"User": user,
                        "Message": message,
                        "Time": time}
        totalList.append(myDictionary)
    #print(myDictionary)
    #print('3. An array of dictionary')
    #print('4. Dump to JSON Object')
    print(json.dumps(totalList, default=str))
    #print('5. print type of content so that the caller can get the JSON Object')


# In[ ]:





# In[26]:


if __name__=="__main__":
    try:
        dbconnection = connectToDb(host="localhost", user="sy306", password="sy306", database="projectdb")
        resultData = selectMessages(dbconnection, 'Messages')
        print("Content-Type: text/html\n")
        sendToWebClient(resultData)
        dbconnection.close()
    except Exception as ex:
        print(ex)
        exit(1)
