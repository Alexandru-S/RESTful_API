"""
The JobTitle Module.

This module contains the JobTitle Class and logic for the
executions to perform as requested.
"""
# coding=utf-8

from web_app import Resource
from web_app import abort
from web_app import reqparse
from .models import JOB_TITLE
from web_app.department.models import DEPARTMENT
from web_app.crud import list_all_join, find_by_join_2
from flask_httpauth import HTTPTokenAuth, HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from web_app import db_creds
auth = HTTPBasicAuth()

users = {db_creds.USERNAME: generate_password_hash(db_creds.PASSWORD)}


@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username


class JobTitle(Resource):
    decorators = [auth.login_required]

    def get(self, var1=None):
        if var1 is None:
            result = list_all_join(JOB_TITLE, DEPARTMENT)
            return result
        if var1 is not None:
            result = find_by_join_2(JOB_TITLE, DEPARTMENT, var1)
            if result is None or len(result) == 0:
                abort(422, message="Could not find any job_titles in that department")
            return result
        else:
            abort(404, message="Could not find data with that id")
