from flask import Flask
from flask_restful import Api, Resource

from .department import Department

app = Flask(__name__)
api = Api(app)

api.add_resource(Department, '/')