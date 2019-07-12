from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms import StringField
from wtforms.validators import Length
from wtforms.validators import NumberRange

class ItemForm(FlaskForm):
    name = StringField('name', validators=[Length(min=0, max=256)])
    quantity = IntegerField('quantity', validators=[NumberRange(min=0)])
    description = StringField('description', validators=[Length(min=0, max=256)])
