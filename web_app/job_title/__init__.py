from web_app import Resource
from web_app import abort
from web_app import reqparse
from .models import JOB_TITLE
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


db_get_args  = reqparse.RequestParser()
db_get_args.add_argument("badge_number", type=int, help="Value of key not int")


class JobTitle(Resource):
    decorators = [auth.login_required]

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
