from application import db
from datetime import datetime

class Task_table(db.Model):
    task_id = db.Column(db.Integer, primary_key = True)
    task_name = db.Column(db.String(20), nullable = False)
    description = db.Column(db.String(50), nullable = False)
    task_status = db.Column(db.Boolean, nullable = False, default = False)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)