from web_app import Resource
from .models import JOB_TITLE
from web_app.crud import list_all


class JobTitle(Resource):
    def get(self):
        result = list_all(JOB_TITLE)
        return result
