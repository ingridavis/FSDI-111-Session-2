#!/usr/bin/env python3
# -*- coding : utf8-*-

""" simple flask app"""

from flask import Flask # importing Flask class from flask module 
#path not properly set up, VSC not picking up virtual environment

app = Flask(__name__) # instantiating app variable with Flask class

from app import routes # importing routes file from app module(folder)

