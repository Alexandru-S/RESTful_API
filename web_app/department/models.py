from web_app import db


class DEPARTMENT(db.Model):
    __tablename__ = 'DEPARTMENT'
    department_code = db.Column(db.Integer, primary_key=True)
    department_name = db.Column(db.String(50))
