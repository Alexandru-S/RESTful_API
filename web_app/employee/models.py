from web_app import db


class EMPLOYEE(db.Model):
    __tablename__ = 'EMPLOYEE'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    badge_number = db.Column(db.Integer)
    country_code = db.Column(db.String(10))
    job_title_code = db.Column(db.Integer)
    start_date = db.Column(db.Date())
    leave_date = db.Column(db.Date())
