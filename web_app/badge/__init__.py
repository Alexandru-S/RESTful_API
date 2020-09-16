from web_app import Resource
from .models import BADGE
from web_app import abort
from web_app.crud import list_all, list_with_var1


class Badge(Resource):
    def get(self, var1=None):
        print('==================', var1)
        if var1 is None:
            result = list_all(BADGE)
            return result

        if var1 == 'active':
            result = list_with_var1(BADGE, BADGE.BADGE_STATUS, BADGE.BADGE_EXPIRY_DATE ,"Active")
            if result is None or len(result) == 0:
                abort(404, message="Could not find any active badges")
            return result
        else:
            abort(404, message="Could not find data with that id")
