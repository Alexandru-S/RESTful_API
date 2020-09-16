import json
import datetime


def date_converter(o):
    if isinstance(o, datetime.date):
        return o.__str__()


def from_sql(row):
    data = row.__dict__.copy()
    data.pop('_sa_instance_state')
    new_data = json.dumps(data, default=date_converter)
    return new_data



def list_all(model):
    query = model.query.all()
    result = list(map(from_sql, query))
    return_result = [json.loads(x) for x in result]
    return return_result
