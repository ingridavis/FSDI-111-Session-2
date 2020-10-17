#!/usr/bin/env python3
# -*- coding : utf8-*-

""" routes file: specifies http routes"""

from app import app  # importing app variable
from flask import g, request #g is global 
import sqlite3

DATABASE = "online_store"

def get_db():
    db = getattr(g, "_database", None) #getting attribute database
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


def get_all_users(): #GET/SCAN/
    cursor = get_db().execute("SELECT * FROM user", ()) 
    results = cursor.fetchall() # returning all the data, PUT, POST
    cursor.close()
    return results

def create_user(): #POST/CREATE
    cursor = get_db().execute("insert into user values", ())
    results = cursor.fetchall()
    cursor.close()
    return results

def get_user(): #GET/READ
    cursor = get_db().execute("SELECT * FROM user where last_name=", ()) 
    if user is None:
        print ('No such user exists')
    results = cursor.fetchall() # returning all the data, PUT, POST
    cursor.close()
    return results

def update_user(): #PUT/UPDATE
    cursor = get_db().execute("update user set", ())
    results = cursor.fetchall()
    cursor.close()
    return results

def delete_user(): #DELETE
    cursor = get_db().execute("delete from user where last_name=", ())
    if user is None:
        print ('No such user exists')
    cursor.close()
    return results


@app.teardown_appcontext 
def close_connection(exception): #closing when app is shut down
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


# @ = decorator that tells flask that when / route is requested, function is called
@app.route('/')
def index():  # function
    return "Hello world"


@app.route('/users', methods=["GET", "POST"]) #SESSION 3 complete at end of class
def get_users():
    # creating an output dictionary 
    out= {"ok": True, "body": ""} # standard formart for our restful API
    body_list = [] # temp list to hold the records we are creating
    if "GET" in request.method:
        raw_data= get_all_users() # getting all users from database, returned to raw data as tuples
        for item in raw_data: # for each item in list of tuples
            temp_dict = {
                "first_name": item[0],
                "last_name": item[1],
                "hobbies": item[2]
            }
            body_list.append(temp_dict) # body list will have all tuples
        out["body"] = body_list # putting body list in body field
        return out

    if "POST" in request.method:
        #create new user
        raw_data= create_user()
        for item in raw_data: # for each item in list of tuples
            temp_dict = {
                "first_name": item[0],
                "last_name": item[1],
                "hobbies": item[2]
            }
            body_list.append(temp_dict) # body list will have all tuples
        out["body"] = body_list # putting body list in body field
        return out

    if "PUT" in request.method:
        raw_data= update_user() 
        for item in raw_data: # for each item in list of tuples
            temp_dict = {
                "first_name": item[0],
                "last_name": item[1],
                "hobbies": item[2]
            }
            body_list.append(temp_dict) # body list will have all tuples
        out["body"] = body_list # putting body list in body field
        return out
    
    if "DELETE" in request.method:
        raw_data= delete_user() 
        for item in raw_data: # for each item in list of tuples
            temp_dict = {
                "first_name": item[0],
                "last_name": item[1],
                "hobbies": item[2]
            }
            body_list.append(temp_dict) # body list will have all tuples
        out["body"] = body_list # putting body list in body field
        return out



@app.route('/aboutme')
def aboutme():
    return {
        'first_name': 'Ingrid',
        'last_name': 'Davis',
        'hobby': 'Outdoor things and photography'
    }

@app.route('/countdown/<int:number>')  # class challenge
def countdown(number):
    return "</br>".join([str(i) for i in range(number, 0, -1)])


@app.route('/agent')
def agent():
    user_agent = request.headers.get("User-Agent")
    return "<p> your user agent is %s</p>" % user_agent

