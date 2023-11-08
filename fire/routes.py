from flask import render_template,request,url_for,redirect,flash
from fire import app
from fire.forms import *
import joblib
import warnings
warnings.filterwarnings("ignore")

@app.route('/')
def home():
    form=PredictForm()
    return render_template('home.html',form=form,predicted_value="NONE")

@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method=='GET':
        return redirect(url_for('home'))
    form = PredictForm()
    model = joblib.load('fire/model')
    try:
        O,T,H = float(form.oxygen.data),float(form.temperature.data),float(form.humidity.data)
    except ValueError:
        flash('Values entered are not numeric! Please enter numeric values!')
        return redirect(url_for('home'))
    form.oxygen.data,form.temperature.data,form.humidity.data="","",""
    predicted_value = model.predict([[O,T,H]])[0]
    return render_template('home.html',predicted_value=predicted_value,form=form)