import db_creds

SQLALCHEMY_DATABASE_URI = ('oracle+cx_oracle://{username}:{password}@{hostname}:{port}/{sid}').format(username=db_creds.USERNAME, password=db_creds.PASSWORD, hostname=db_creds.HOSTNAME, port=db_creds.PORT, sid=db_creds.SID)