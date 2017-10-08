# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.pymongo import PyMongo
from flask.ext.login import LoginManager

client = Flask(__name__)

bs = Bootstrap(client) #flask-bootstrap

#Configuration of application, see configuration.py, choose one and uncomment.
#app.config.from_object('configuration.ProductionConfig')
client.config.from_object('client.configuration.DevelopmentConfig')
#app.config.from_object('configuration.TestingConfig')

from client import views