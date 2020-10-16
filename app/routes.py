#!/usr/bin/env python3
# -*- coding : utf8-*-

""" routes file: specifies http routes"""

from flask import g
from app import app  # importing app variable
import sqlite3

from flask import request

DATABASE = "online_store"


def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


def get_all_users():
    cursor = get_db().execute("SELECT * FROM user", ())
    results = cursor.fetchall()
    cursor.close()
    return results


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


# @ = decorator that tells flask that when / route is requested, function is called
@app.route('/')
def index():  # function
    return "Hello world"


"""
@app.route('/users', methods=["GET", "POST"]) #SESSION 3 complete at end of class
def get_users():
    out= {"ok": True, "body": ""}
    body_list = []
    if "GET" in request.method:
        raw_data= get_all_users()
    if "POST" in method:
        #create new user
        pass
"""


@app.route('/aboutme')
def aboutme():
    return {
        'first_name': 'Ingrid',
        'last_name': 'Davis',
        'hobby': 'Outdoors and photography'
    }


@app.route('/countdown/<int:number>')  # class challenge
def countdown(number):
    return "</br>".join([str(i) for i in range(number, 0, -1)])


@app.route('/agent')
def agent():
    user_agent = request.headers.get("User-Agent")
    return "<p> your user agent is %s</p>" % user_agent
