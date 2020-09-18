"""
The Badge Module.

This module contains the Badge Class and logic for the
executions to perform as requested.
"""
# coding=utf-8

from web_app import Resource
from .models import BADGE
from web_app import abort
from web_app import reqparse
from web_app.crud import list_all, list_with_var1, list_with_number
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
db_get_args.add_argument("badge_number", type=int, help="Value of key not int")

class Badge(Resource):
    decorators = [auth.login_required]

    def get(self, var1=None):
        args = db_get_args.parse_args()

        if args.badge_number is not None:
            result = list_with_number(BADGE, BADGE.badge_number, args.badge_number)
            if result is None or len(result) == 0:
                abort(404, message="Could not find any badges with that id")
            return result

        if var1 is None:
            result = list_all(BADGE)
            return result

        if var1 == 'active':
            result = list_with_var1(BADGE, BADGE.badge_status, BADGE.badge_expiry_date, "Active")
            if result is None or len(result) == 0:
                abort(404, message="Could not find any active badges")
            return result
        else:
            abort(404, message="Could not find data with that id")
