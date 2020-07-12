from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from fask_marshmallow import Marshmallow
import os


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')


db = SQLAlchemy(app)
ma = Marshmallow(app)

