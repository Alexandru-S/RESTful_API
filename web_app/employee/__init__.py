"""
The Employee Module.

This module contains the Employee Class and logic for the
executions to perform as requested.
"""
# coding=utf-8


from web_app import Resource
from .models import EMPLOYEE
from web_app.job_title.models import JOB_TITLE
from web_app.department.models import DEPARTMENT
from web_app import abort
from web_app import reqparse
from web_app.crud import  check_with_var1, find_by_join, list_all_employees
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from web_app import db_creds
auth = HTTPBasicAuth()

users = { db_creds.USERNAME: generate_password_hash(db_creds.PASSWORD)}


@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username


db_get_args  = reqparse.RequestParser()
db_get_args.add_argument("department_name", type=str, help="Value of key not int")


class Employee(Resource):
    def get(self, var1=None):
        decorators = [auth.login_required]

        args = db_get_args.parse_args()
        if args.department_name is not None:
            result = find_by_join(EMPLOYEE, JOB_TITLE, DEPARTMENT, args.department_name)
            if result is None or len(result) == 0:
                abort(422, message="Could not find any employees in that department")
            return result
        if var1 is None:
            result = list_all_employees(EMPLOYEE, JOB_TITLE, DEPARTMENT)
            return result
        if var1 == 'active':
            result = check_with_var1(EMPLOYEE, JOB_TITLE, DEPARTMENT, EMPLOYEE.leave_date, None)
            if result is None or len(result) == 0:
                abort(404, message="Could not find any active employees")
            return result
        else:
            abort(404, message="Could not find data with that id")
