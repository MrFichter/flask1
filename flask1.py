#! /usr/bin/python

# all the imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from contextlib import closing

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

#initialize database

def init_db():
	with closing (connect_db()) as db:
		with app.open_resource('schema.sql') as f:
			db.cursor().executescript(f.read())
		db.commit()
	# The tutorial wants me to run init_db once from the command line
	# but does not want me to put an init_db line into the program.

#The line below checks "if we are running the module by itself or importing.
#See explanation here: http://marakana.com/forums/python/python/116.html
 
if __name__ == '__main__':
	app.run()

