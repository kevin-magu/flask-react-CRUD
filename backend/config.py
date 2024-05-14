from flask import Flask
from flask_mysqldb import MySQL
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# MySQL configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'Contact'  # Change to your database name
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'  # Return results as dictionaries

# Initialize MySQL
mysql = MySQL(app)
