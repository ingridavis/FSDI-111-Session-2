#!/usr/bin/env python3
# -*- coding : utf8-*-

""" routes file: specifies http routes"""

from app import app  # importing app variable
from flask import g, request, render_template, redirect, url_for, session#g is global 
from app.forms.name import NameForm
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

"""

def get_user(): #GET/READ
    cursor = get_db().execute("SELECT * FROM user where last_name=", ()) 
    if user is None:
        print ('No such user exists')
    results = cursor.fetchall() # returning all the data, PUT, POST
    cursor.close()
    return results
"""

def create_user(user):
    sql = """INSERT INTO user (
                    first_name,
                    last_name,
                    hobbies)
            VALUES (?, ?, ?)""" # ? are placeholders
    cursor = get_db()
    cursor.execute(sql, user) # takes user and match up to the columns
    cursor.commit()
    
    return True       # We're just returning true.
"""
def delete_user(user): #DELETE
    
    sql = ""DELETE from user where last_name=(
                    last_name)
            VALUES (?)""
    cursor = get_db()
    cursor.execute(sql, user)
    cursor.delete
    cursor.commit()# commit = save it in the database
    if user is None:
        print ('No such user exists')
    cursor.close()
    # return cursor.lastrowid           # We could do this, but we won't for now because our app doesn't need it.
    return True        
"""

# connecting to html page

@app.route("/scan/users")
def scan_users():
    users = get_all_users()
    return render_template("scan_users.html", users=users)

"""

@app.route("/delete/users")
def del_user():
    users = delete_user()
    return render_template("delete_user.html", users=users)

"""


# Closing when app is shut down
@app.teardown_appcontext 
def close_connection(exception): 
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()

# index page
# @ = decorator that tells flask that when / route is requested, function is called
@app.route('/')
def index():  # function
    return "Hello world"

# Users route 
@app.route('/users', methods=["GET", "POST"]) #SESSION 3 complete at end of class
def get_users():
    # creating an output dictionary 
    out= {"ok": True, "body": ""} # standard formart for our restful API
    body_list = [] # temp list to hold the records we are creating
    if "GET" in request.method:
        form = NameForm()
        raw_data= get_all_users() # getting all users from database, returned to raw data as tuples
        for item in raw_data: # for each item in list of tuples
            temp_dict = {
                "first_name": item[0],
                "last_name": item[1],
                "hobbies": item[2]
            }
            body_list.append(temp_dict) # body list will have all tuples
        out["body"] = body_list # putting body list in body field
        return render_template(
            "about_me.html",
            
            first_name = out["body"][0].get("first_name"),
            last_name = out["body"][0].get("last_name"),
            hobbies = out["body"][0].get("hobbies"),
            form=form
        )
    if "POST" in request.method:
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        hobbies = request.form.get("hobbies")
        create_user((first_name, last_name, hobbies))
        
        return redirect(url_for("get_users"))
"""
    if "DELETE" in request.method: 
        #display users 
       
        # if sumbit(delete) button is clicked, delete user
        delete_user((first_name, last_name, hobbies))
"""        
      
 



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

@app.errorhandler(404)
def page_not_found(exception):
    return render_template("404.html"), 404

@app.errorhandler(500)
def server_error(exception):
    return render_template("500.html"), 500

