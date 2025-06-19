from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Optional  # Ensure Optional is imported

class StationeryForm(FlaskForm):
    item_type = SelectField('Item Type', choices=[
        ('A4', 'A4 Paper'),
        ('A3', 'A3 Paper'),
        ('A5', 'A5 Paper'),
        ('photo_paper', 'Photo Paper')
    ], validators=[DataRequired()])
    
    quantity = IntegerField('Initial Quantity', validators=[DataRequired(), NumberRange(min=0)])
    
    unit = SelectField('Unit', choices=[
        ('sheets', 'Sheets'),
        ('reams', 'Reams (500 sheets)'),
        ('boxes', 'Boxes')
    ], validators=[DataRequired()])
    
    threshold = IntegerField('Low Stock Threshold', validators=[DataRequired(), NumberRange(min=0)])
    
    location = SelectField('Location', choices=[
        ('', 'General Storage'),
        ('Mamal Boys Lab', 'Mamal Boys Lab'),
        ('Mamal Girls Lab', 'Mamal Girls Lab'),
        ('Masakin', 'Masakin'),
        ('Rabaat', 'Rabaat')
    ], validators=[Optional()])
    
    submit = SubmitField('Add Item')


class StationeryUpdateForm(FlaskForm):
    quantity_change = IntegerField('Quantity Change', validators=[DataRequired(), NumberRange(min=1)], default=1)
    
    action = SelectField('Action', choices=[
        ('add', 'Add Stock'),
        ('subtract', 'Use Stock')
    ], validators=[DataRequired()])
    
    threshold = IntegerField('Update Threshold', validators=[Optional(), NumberRange(min=0)])
    
    location = SelectField('Update Location', choices=[
        ('', 'No Change'),
        ('Mamal Boys Lab', 'Mamal Boys Lab'),
        ('Mamal Girls Lab', 'Mamal Girls Lab'),
        ('Masakin', 'Masakin'),
        ('Rabaat', 'Rabaat')
    ], validators=[Optional()])
    
    submit = SubmitField('Update Item')
