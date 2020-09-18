"""
The Department Module.

This module contains the Department Class and logic for the
executions to perform as requested.
"""
# coding=utf-8

from web_app import Resource
from web_app import auth
from .models import DEPARTMENT
from web_app.crud import list_all


class Department(Resource):
    decorators = [auth.login_required]

    def get(self):
        result = list_all(DEPARTMENT)
        return result
