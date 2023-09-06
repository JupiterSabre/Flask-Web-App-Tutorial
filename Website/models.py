#  ( . ) refers to current package (website)
# flask_login is module for logins
from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func



class Member(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    bike_shop = db.Column(db.String(150))
    bikes_shared = db.relationship("Bike")


class Bike(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey("member.id"))
    # current_borrower: db.Column(db.Integer, db.ForeignKey("member.id"))
    # bike_shop = db.Column(db.String, db.ForeignKey("member.bike_shop"))
    manufacture = db.Column(db.String(45))
    lock_combo = db.Column(db.String(100))
    type = db.Column(db.String(45))
    date_registered = db.Column(db.DateTime(timezone=True), default=func.now)
    current_borrow_status = db.Column(db.DateTime(timezone=True), default=func.now)
    
    
class Borrow_Session (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner_email = db.Column(db.String, db.ForeignKey("member.email"))
    borrower_id = db.Column(db.Integer, db.ForeignKey("member.id"))