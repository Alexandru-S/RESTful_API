from web_app import Resource


class Department(Resource):
    def get(self):
        return {"title":"Department Class Works"}