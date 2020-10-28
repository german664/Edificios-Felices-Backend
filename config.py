from os import environ
import json
from flask import Flask, request, jsonify, render_template
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_cors import CORS
import pymysql


class Base:
    DEBUG = False
    ENV = 'production'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    JWT_SECRET_KEY = "33b9b3de94a42d19f47df7021954eaa8"
    UPLOAD_FOLDER = "static"


class Development(Base):
    DEBUG = True
    ENV = 'development'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # mysql+pymysql://<username>:<password>@<host_ip>:<port>/<database_name>
    # if environ.get('DATABASE_URL'):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://b48ea3b8ed27a8:0b7c4f87@eu-cdbr-west-03.cleardb.net/heroku_841a994e33824ed'
    # else:
    #    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Nico2010!@localhost:3306/edificios_felices'
    JWT_SECRET_KEY = "ba2c9a390a763c9ac2c1a1071652d21a"
    UPLOAD_FOLDER = "static"
