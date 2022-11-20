from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_cors import *

db = SQLAlchemy()
HOSTNAME = 'comp9900database.cugl4hvapyl5.ap-northeast-1.rds.amazonaws.com'
PORT = '3306'
DATABASE = 'comp9900_db'
USERNAME = 'root'
PASSWORD = 'comp9900'
DB_URL = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)


def create_app():
    # create a flask object
    app = Flask(__name__)
    CORS(app, supports_credentials=True)

    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = "9900_sunflower"
    app.config['JSON_SORT_KEYS'] = False
    db.init_app(app)
    return app