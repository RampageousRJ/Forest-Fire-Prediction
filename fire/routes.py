from flask import render_template
from fire import app

@app.route('/')
def home():
    return render_template('home.html')