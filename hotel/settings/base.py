import os
from flask.ext.api import FlaskAPI
from flask.ext.mysqldb import MySQL

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEBUG = False

app = FlaskAPI(__name__)
mysql = MySQL(app)
