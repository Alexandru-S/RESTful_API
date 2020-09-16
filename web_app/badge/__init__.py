from web_app import Resource
from .models import BADGE
from web_app import abort
from web_app import reqparse
from web_app.crud import list_all, list_with_var1, list_with_number

db_get_args  = reqparse.RequestParser()
db_get_args.add_argument("badge_number", type=int, help="Value of key not int")

class Badge(Resource):
    def get(self, var1=None):
        args = db_get_args.parse_args()
        if args.badge_number is not None:
            result = list_with_number(BADGE, BADGE.BADGE_NUMBER, args.badge_number)
            return result

        if var1 is None:
            result = list_all(BADGE)
            return result

        if var1 == 'active':
            result = list_with_var1(BADGE, BADGE.BADGE_STATUS, BADGE.BADGE_EXPIRY_DATE,"Active")
            if result is None or len(result) == 0:
                abort(404, message="Could not find any active badges")
            return result
        else:
            abort(404, message="Could not find data with that id")
