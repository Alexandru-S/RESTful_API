import pandas as pd
import logging
import config
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from .department import Department
from .badge import Badge
from .employee import Employee
from .job_title import JobTitle

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI


db.init_app(app)

api.add_resource(Department, '/department')
api.add_resource(Badge, '/badges', '/badges/<string:var1>', '/badges?badge_number=<int:badgeid>')
api.add_resource(Employee, '/employees')
api.add_resource(JobTitle, '/job_titles', '/job_titles/<string:active>')