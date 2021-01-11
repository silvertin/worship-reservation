from w_reservation import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    admin = db.Column(db.Integer, nullable=True, server_default='2')


class Worship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date(), nullable=False)
    part = db.Column(db.String(100), nullable=False)
    limit = db.Column(db.Integer, nullable=False)
    curnum = db.Column(db.Integer, nullable=False)


class Seat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(10), nullable=False)
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id',ondelete='CASCADE'), nullable=True, server_default='1')
    # user = db.relationship('User', backref=db.backref('seat_set'))
    user = db.Column(db.String(50), nullable=True)
    worship_id = db.Column(db.Integer, db.ForeignKey('worship.id',ondelete='CASCADE'), nullable=False)
    worship = db.relationship('Worship', backref=db.backref('seat_set', cascade='all, delete-orphan', order_by=user))






