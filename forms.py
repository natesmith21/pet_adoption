from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SelectField
from wtforms.validators import InputRequired, Optional, URL, NumberRange



pet_species = ['Dog', 'Cat', 'Porcupine']

class AddPetForm(FlaskForm):
    """a form to create new pets for adoption"""
    name = StringField('Name', validators=[InputRequired()])
    species = SelectField('Species', choices=pet_species, validators=[InputRequired()])
    photo_url = StringField('Pets Photo (URL)', validators=[URL(), Optional()])
    age = IntegerField('Age', validators=[Optional(), NumberRange(min=1, max=30, message=f'please enter an age between {min} and {max}')])
    note = StringField('Notes')


class EditPetForm(FlaskForm):
    """a form to edit adoptable pets + mark them adopted"""
    name = StringField('Name', validators=[InputRequired()])
    species = SelectField('Species', choices=pet_species, validators=[InputRequired()])
    photo_url = StringField('Pets Photo (URL)', validators=[URL(), Optional()])
    age = IntegerField('Age', validators=[Optional(), NumberRange(min=1, max=30, message=f'please enter an age between {min} and {max}')])
    note = StringField('Notes')
    adopted = BooleanField('adopted')


