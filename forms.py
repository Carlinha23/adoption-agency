from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField, TextAreaField
from wtforms.validators import InputRequired, URL, Email, Optional, NumberRange, DataRequired


class AddPetForm(FlaskForm):
    name = StringField('Pet Name', validators=[InputRequired()])
    species = SelectField('Species', choices=[('dog', 'Dog'), ('cat', 'Cat'), ('other', 'Other')],
                          validators=[InputRequired()])
    photo_url = StringField('Photo URL', validators=[Optional(), URL()])
    age = IntegerField('Age', validators=[NumberRange(min=0, max=30)])
    notes = TextAreaField('Notes', validators=[Optional()])
    available = BooleanField('Available for Adoption', default=True)

class EditPetForm(FlaskForm):
    photo_url = StringField('Photo URL', validators=[Optional(), URL()])
    notes = TextAreaField('Notes', validators=[Optional()])
    available = BooleanField('Available')