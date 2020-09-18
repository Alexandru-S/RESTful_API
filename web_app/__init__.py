import logging
import config
from . import db_creds
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
db = SQLAlchemy()
auth = HTTPBasicAuth()

from .department import Department
from .employee import Employee
from .badge import Badge
from .job_title import JobTitle

app = Flask(__name__)
api = Api(app)


users = { db_creds.USERNAME: generate_password_hash(db_creds.PASSWORD)}

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username


api.add_resource(Department, '/department')
api.add_resource(Badge, '/badges', '/badges/<string:var1>')
api.add_resource(Employee, '/employees', '/employees/<string:var1>')
api.add_resource(JobTitle, '/job_titles', '/job_titles/<string:var1>')


def create_app(config_name):
    app.config['SQLALCHEMY_DATABASE_URI'] = config_name.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    return app
