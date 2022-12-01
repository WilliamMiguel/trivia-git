# from pymongo import MongoClient
# from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy

# client = MongoClient('localhost', 27017)

# db = client['TriviaProtestante']
db = SQLAlchemy()