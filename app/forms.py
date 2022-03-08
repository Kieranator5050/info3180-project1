from numbers import Number
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, IntegerField, DecimalField, SelectField, TextAreaField, FileField
from wtforms.validators import InputRequired

class PropertyForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    noBedRooms = IntegerField('No. of Bedrooms', validators=[InputRequired()])
    noBathRooms = IntegerField('No. of Bathrooms', validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])
    price = DecimalField('Price', validators=[InputRequired()])
    type = SelectField('Type', choices=[("House","House"),("Apartment","Apartment")], validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    photo = FileField('Photo', 
                            validators=[
                                FileRequired(), 
                                FileAllowed(['jpg','png','jpeg','jfif'], "Only Images!" ),
                                InputRequired()
                                ])