from flask import Flask,request,render_template
import os
import numpy as np
import pandas as pd
import pickle 



# Get the absolute path of model.pkl
model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')
model_tranform=os.path.join(os.path.dirname(__file__), 'transformer.pkl')

# loading model
# model = pickle.load(open('model.pkl','rb'))
# Load the model safely
with open(model_path, 'rb') as f:
    model = pickle.load(f)

with open(model_tranform, 'rb') as f:
    pt = pickle.load(f)

#create flask app
app=Flask(__name__)

#route
@app.route('/')
def index():
    return render_template("index.html")
@app.route("/predict", methods=['POST'])
def predict():
    #   cement    blastFurnace    flyAsh    water    superplasticizer    courseAggregate    fineaggregate    age
    cement = float(request.form['cement'])
    blastFurnace = float(request.form['blastFurnace'])
    flyAsh = float(request.form['flyAsh'])
    water = float(request.form['water'])
    superplasticizer = float(request.form['superplasticizer'])
    courseAggregate = float(request.form['courseAggregate'])
    fineaggregate = float(request.form['fineaggregate'])
    age = int(request.form['age'])


# transform input features
    features = np.array([cement, blastFurnace, flyAsh, water, superplasticizer, courseAggregate, fineaggregate, age]).reshape(1, -1)
    
    # transform inputs
    features_transformed = pt.transform(features)
    prediction = model.predict(features_transformed).reshape(1, -1)

    return render_template('index.html', strength=prediction[0][0])



#pythoon main
if __name__=="__main__":
    app.run(debug=True)