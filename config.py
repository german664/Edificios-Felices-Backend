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
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Nico2010!@localhost:3306/edificios_'
    JWT_SECRET_KEY = "ba2c9a390a763c9ac2c1a1071652d21a"
    UPLOAD_FOLDER = "static"
