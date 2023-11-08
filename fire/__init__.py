from flask import Flask
from fire.forms import *

app = Flask(__name__)

from fire.routes import *