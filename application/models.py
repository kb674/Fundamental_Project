from application import db
from datetime import datetime
   
class Boarders(db.Model):
    boarder_id = db.Column(db.Integer, primary_key = True)
    boarder_name = db.Column(db.String(100), nullable = False)
    tricks = db.relationship('Tricks', backref='boarder')

class Tricks(db.Model):
    trick_id = db.Column(db.Integer, primary_key = True)
    trick_name = db.Column(db.String(50), nullable = False)
    fk_boarder_id = db.Column(db.Integer, db.ForeignKey('boarders.boarder_id'), nullable = True)

