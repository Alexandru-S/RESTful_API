from web_app import db


class BADGE(db.Model):
    __tablename__ = 'BADGE'
    BADGE_NUMBER = db.Column(db.Integer, primary_key=True)
    BADGE_STATUS = db.Column(db.String(10))
    BADGE_EXPIRY_DATE = db.Column(db.Date())