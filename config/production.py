from config.default import *


SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR,'w_reservation.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\xaf>\xb6\xc0-_\x0c\x9a\xde\r\x0c\x83&\xed\x9e\xc4'
