#! /usr/bin/python

# all the imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

# configuration
DATABASE = '/tmp/flask1.db'
DEBUG = False #The tutorial set this to True but warned about keeping this way.
SECRET_KEY = 'TO BE EXTRA SAFE, DO NOT POST THIS ON GITHUB'
USERNAME = 'admin'
PASSWORD = 'TO BE EXTRA SAFE, DO NOT POST THIS ON GITHUB'

# create an application using some things from the Flask class we imported above.

app = Flask(__name__)
app.config.from_object(__name__)

#The function below connects to the database at /tmp/flask1.db (see above).

def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

#The line below lets you run the file as a standalone application.
#(If you want.)
if __name__ == '__main__':
	app.run()


