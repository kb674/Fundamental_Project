from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class TaskForm(FlaskForm):
    boarder_name = StringField('Name of the boarder: ')
    submit = SubmitField('Add Boarder')