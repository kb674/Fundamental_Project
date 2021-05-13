from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField

class TaskForm(FlaskForm):
    boarder_name = StringField('Name of the boarder: ')
    submit = SubmitField('Add Boarder')

class TrickForm(FlaskForm):
    trick_name = StringField('Name of trick: ')
    fk_boarder_id = IntegerField('Boarder number: ')
    submit = SubmitField('Add Trick')