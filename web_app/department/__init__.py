from web_app import Resource
from .models import DEPARTMENT
from web_app.crud import list_all


class Department(Resource):
    def get(self):
        result = list_all(DEPARTMENT)
        return result
