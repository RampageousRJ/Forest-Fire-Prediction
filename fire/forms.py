from wtforms import FloatField,SubmitField
from wtforms.validators import DataRequired
from flask_wtf import RecaptchaField,FlaskForm

class PredictForm(FlaskForm):
    oxygen = FloatField(label='Oxygen Level',validators=[DataRequired()])
    temperature = FloatField(label='Temperature',validators=[DataRequired()])
    humidity = FloatField(label='Humidity Level',validators=[DataRequired()])
    recaptcha = RecaptchaField()
    submit = SubmitField(label='Predict')