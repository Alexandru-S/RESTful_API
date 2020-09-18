from web_app import db


class EMPLOYEE(db.Model):
    __tablename__ = 'EMPLOYEE'
    ID = db.Column(db.Integer, primary_key=True)
    FIRSTNAME = db.Column(db.String(100))
    LASTNAME = db.Column(db.String(100))
    BADGE_NUMBER = db.Column(db.Integer)
    COUNTRY_CODE = db.Column(db.String(10))
    JOB_TITLE_CODE = db.Column(db.Integer)
    START_DATE = db.Column(db.Date())
    LEAVE_DATE = db.Column(db.Date())
