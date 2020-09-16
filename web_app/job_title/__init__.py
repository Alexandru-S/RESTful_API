from web_app import Resource
from web_app import abort
from .models import JOB_TITLE
from web_app.crud import list_all


class JobTitle(Resource):
    def get(self, active=None):
        print('ACTIVE'*40, type(active))
        if active is None:
            result = list_all(JOB_TITLE)
            return result

        if active == 'active':
            #result = list_with_var1(JOB_TITLE, active)
            return {'new':'videos active'}
        else:
            abort(404, message="Could not find data with that id")
