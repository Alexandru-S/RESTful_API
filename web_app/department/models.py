'''from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()'''
from web_app import db


class DEPARTMENT(db.Model):
    __tablename__ = 'DEPARTMENT'
    DEPARTMENT_CODE = db.Column(db.Integer, primary_key=True)
    DEPARTMENT_NAME = db.Column(db.String(50))