"""Forms for pet adoption app"""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField
from wtforms.validators import InputRequired, Optional, NumberRange, URL, AnyOf

class AddPetForm(FlaskForm):
    """Form for adding a new pet"""
    name = StringField("Pet Name",
                       validators=[InputRequired()])
    species = StringField("Pet Species",
                          validators=[AnyOf(values=["cat", "dog", "porcupine"])])
    photo_url = StringField("Pet Photo",
                            validators=[Optional(), URL()])
    age = FloatField("Pet Age",
                     validators=[Optional(), NumberRange(min=0, max=30)])
    notes = StringField("Additional Notes",
                        validators=[Optional()])
    
class EditPetForm(FlaskForm):
    """Form for editing an existing pet"""
    photo_url = StringField('Pet Photo',
                            validators=[Optional(), URL()])
    notes = StringField('Pet Notes',
                        validators=[Optional()])
    available = BooleanField('Pet Available?')
