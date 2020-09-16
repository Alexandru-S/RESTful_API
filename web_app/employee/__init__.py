from web_app import Resource
from .models import EMPLOYEE
from web_app.crud import list_all


class Employee(Resource):
    def get(self):
        result = list_all(EMPLOYEE)
        return result
