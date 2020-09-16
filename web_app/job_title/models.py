from web_app import db


class JOB_TITLE(db.Model):
    __tablename__ = 'JOB_TITLE'
    JOB_TITLE_CODE = db.Column(db.Integer, primary_key=True)
    JOB_TITLE_NAME = db.Column(db.String(50))
    DEPARTMENT_CODE = db.Column(db.Integer)