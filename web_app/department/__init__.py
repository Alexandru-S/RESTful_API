"""
The Department Module.

This module contains the Department Class and logic for the
executions to perform as requested.
"""
# coding=utf-8

from web_app import Resource
from .models import DEPARTMENT
from web_app.crud import list_all
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from web_app import db_creds
auth = HTTPBasicAuth()

users = {db_creds.USERNAME: generate_password_hash(db_creds.PASSWORD)}


@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username


class Department(Resource):
    decorators = [auth.login_required]

    def get(self):
        result = list_all(DEPARTMENT)
        return result
