from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
from flask_wtf import RecaptchaField,FlaskForm

class PredictForm(FlaskForm):
    oxygen = StringField(label='Oxygen Level',validators=[DataRequired()])
    temperature = StringField(label='Temperature',validators=[DataRequired()])
    humidity = StringField(label='Humidity Level',validators=[DataRequired()])
    recaptcha = RecaptchaField()
    submit = SubmitField(label='Predict')