from web_app import Resource
from .models import BADGE
from web_app.crud import list_all


class Badge(Resource):
    def get(self):
        result = list_all(BADGE)
        return result