from web_app import Resource
from .models import EMPLOYEE
from web_app.job_title.models import JOB_TITLE
from web_app.department.models import DEPARTMENT
from web_app import abort
from web_app import reqparse
from web_app.crud import list_all, check_with_var1, find_by_join

db_get_args  = reqparse.RequestParser()
db_get_args.add_argument("department_name", type=str, help="Value of key not int")


class Employee(Resource):
    def get(self, var1=None):
        args = db_get_args.parse_args()
        if args.department_name is not None:
            result = find_by_join(EMPLOYEE, JOB_TITLE, DEPARTMENT, args.department_name)
            print('RESULT', result)
            return result
        if var1 is None:
            result = list_all(EMPLOYEE)
            return result
        if var1 == 'active':
            print('X'*20)
            result = check_with_var1(EMPLOYEE, EMPLOYEE.LEAVE_DATE, EMPLOYEE.LEAVE_DATE,None)
            if result is None or len(result) == 0:
                abort(404, message="Could not find any active badges")
            return result
