from unittest import result
from flask import Flask,request,render_template,flash,url_for,redirect
from streamlit import form
import pickle
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 

#=================================Create App ============
app=Flask(__name__)


#==================================Loading Model ===========

rfc=pickle.load(open('models/model.pkl','rb'))
scaler=pickle.load(open('models/scaler.pkl','rb'))


#=====================prediction function====================================================
def prediction(sl_no, gender, ssc_p, hsc_p, degree_p, workex, etest_p, specialisation, mba_p):
    data = {
    'sl_no': [sl_no],
    'gender': [gender],
    'ssc_p': [ssc_p],
    'hsc_p': [hsc_p],
    'degree_p': [degree_p],
    'workex': [workex],
    'etest_p': [etest_p],
    'specialisation': [specialisation],
    'mba_p': [mba_p]
    }
    data = pd.DataFrame(data)
    data['gender'] = data['gender'].map({'Male':1,"Female":0})
    data['workex'] = data['workex'].map({"Yes":1,"No":0})
    data['specialisation'] = data['specialisation'].map({"Mkt&HR":1,"Mkt&Fin":0})
    scaled_df = scaler.transform(data)
    result = rfc.predict(scaled_df).reshape(1, -1)
    return result[0]



@app.route("/")
def index():
    return render_template('index.html')

@app.route('/index')
def home():
    return render_template("index.html")

@app.route('/job')
def job():
    return render_template('job.html')

@app.route('/ana')
def job():
    return render_template('ana.html')

@app.route("/placement", methods=['POST','GET'])
def pred():
    if request.method == 'POST':
        sl_no = request.form['sl_no']
        gender = request.form['gender']
        ssc_p = request.form['ssc_p']
        hsc_p = request.form['hsc_p']
        degree_p = request.form['degree_p']
        workex = request.form['workex']
        etest_p = request.form['etest_p']
        specialisation = request.form['specialisation']
        mba_p = request.form['mba_p']
      
        # result = prediction(sl_no, gender, ssc_p, hsc_p, degree_p, workex, etest_p, specialisation, mba_p)
        result = prediction(sl_no, gender, ssc_p, hsc_p, degree_p, workex, etest_p, specialisation, mba_p)

        if result == 1:
            pred = "Placed"
            rec = "We recommend you that this is the best candidate for you business"
            return render_template('job.html', result=pred, rec=rec)

        else:
            pred = "Not Placed"
            rec = "We recommend you that this is not the best candidate for your business"
            return render_template('job.html', result=pred,rec=rec)
       
   



if __name__=="__main__":
    app.run(debug=True)