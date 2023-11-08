from flask import Flask
from fire.forms import *
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)
app.config['RECAPTCHA_PRIVATE_KEY'] = os.getenv('PREDICTOR_PRIVATE_KEY')
app.config['RECAPTCHA_PUBLIC_KEY'] = os.getenv('PREDICTOR_PUBLIC_KEY')
app.config['SECRET_KEY'] = os.getenv('PREDICTOR_SECRET_KEY')

from fire.routes import *