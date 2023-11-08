from flask import render_template,request,url_for,redirect
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
    predicted_value = model.predict([[form.oxygen.data,form.temperature.data,form.humidity.data]])[0]
    form.oxygen.data,form.temperature.data,form.humidity.data="","",""
    return render_template('home.html',predicted_value=predicted_value,form=form)