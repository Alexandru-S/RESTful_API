import json
import datetime
import requests
from web_app import db
from sqlalchemy import and_, or_


def add_keys_helper(model2, model3, result):
    query2 = dict(model2.query.with_entities(model2.JOB_TITLE_CODE, model2.JOB_TITLE_NAME).distinct().all())
    for x in result:
        if 'JOB_TITLE_CODE' in x.keys():
            x['JOB_TITLE'] = query2[x['JOB_TITLE_CODE']]
            x.pop('JOB_TITLE_CODE')

        if 'JOB_TITLE' in x.keys():
            dep_code = model2.query.filter(model2.JOB_TITLE_NAME == x['JOB_TITLE']).first().DEPARTMENT_CODE
            dep_name = model3.query.filter(model3.DEPARTMENT_CODE == dep_code).first().DEPARTMENT_NAME
            x['DEPARTMENT_NAME'] = dep_name
    return result


def date_converter(o):
    if isinstance(o, datetime.date):
        return o.__str__()


def from_sql(row):
    data = row.__dict__.copy()
    data.pop('_sa_instance_state')
    new_data = json.dumps(data, default=date_converter)
    new_new_data = json.loads(new_data)
    if 'COUNTRY_CODE' in new_new_data.keys():
        URL = ('https://restcountries.eu/rest/v2/alpha?codes={code1};{code1};{code1}').format(code1 = row.COUNTRY_CODE)
        data = requests.get(url=URL).json()
        new_new_data['COUNTRY'] = data[0]['name']
        new_new_data.pop('COUNTRY_CODE')
    return new_new_data


def list_all(model):
    query = model.query.all()
    result = list(map(from_sql, query))
    return result


def list_all_employees(model1, model2, model3):
    query = model1.query.all()
    result = add_keys_helper(model2, model3, list(map(from_sql, query)))
    return result


def list_all_join(model1, model2):
    query = db.session.query(model1).filter(model2.DEPARTMENT_CODE == model1.DEPARTMENT_CODE).all()
    result = list(map(from_sql, query))
    query2 = dict(model2.query.with_entities(model2.DEPARTMENT_NAME, model2.DEPARTMENT_CODE).distinct().all())
    for x in result:
        if 'DEPARTMENT_CODE' in x.keys():
            x['DEPARTMENT_NAME'] = list(query2.keys())[list(query2.values()).index(x['DEPARTMENT_CODE'])]
            x.pop('DEPARTMENT_CODE')
    return result


def list_with_number(model, keyz, varnum):
    query = model.query.filter(keyz == varnum).all()
    result = list(map(from_sql, query))
    return result


def list_with_var1(model, keyz, date_limit, var1):
    query = model.query.filter(and_(keyz == var1, date_limit > datetime.date.today())).all()
    result = list(map(from_sql, query))
    return result


def check_with_var1(model, model2, model3, date_limit, var1):
    query = model.query.filter(or_(date_limit == var1, date_limit < datetime.date.today())).all()
    result = add_keys_helper(model2, model3, list(map(from_sql, query)))
    return result


def find_by_join(model1, model2, model3, var2):
    query = db.session.query(model1).filter(model3.DEPARTMENT_NAME == var2).filter(model3.DEPARTMENT_CODE == model2.DEPARTMENT_CODE).filter(model2.JOB_TITLE_CODE == model1.JOB_TITLE_CODE).all()
    result = add_keys_helper(model2, model3, list(map(from_sql, query)))
    return result


def find_by_join_2(model1, model2, var1):
    query = db.session.query(model1).filter(model2.DEPARTMENT_NAME == var1).filter(model2.DEPARTMENT_CODE == model1.DEPARTMENT_CODE).all()
    result = list(map(from_sql, query))
    query2 = dict(model2.query.with_entities(model2.DEPARTMENT_NAME, model2.DEPARTMENT_CODE).distinct().all())
    for x in result:
        if 'DEPARTMENT_CODE' in x.keys():
            x['DEPARTMENT_NAME'] = list(query2.keys())[list(query2.values()).index(x['DEPARTMENT_CODE'])]
            x.pop('DEPARTMENT_CODE')
    return result

