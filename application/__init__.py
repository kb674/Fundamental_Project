from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv(one)
app.config["SECRET_KEY"] = getenv(two)
db = SQLAlchemy(app)

from application import routes



