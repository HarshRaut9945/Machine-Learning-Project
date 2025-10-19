from os import name
import os
from flask import Flask, request, render_template
import pickle
import numpy as np

model_path = os.path.join(r"C:\Users\Lenovo\OneDrive\Desktop\Machine LEarning PRoject\Market_Sale_pred", "model.pkl")


# pickle.load(open('model.pkl','rb'))
with open(model_path, 'rb') as file:
    model = pickle.load(file)

app=Flask(__name__)

def preprocess_input(input_str):
    input_list = input_str.split(',')
    input_array = np.array(input_list, dtype=np.float32)
    return input_array.reshape(1, -1)

#flask app
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict',methods=['POST'])
def predict():
    input_str = request.form['input_string']
    input_array = preprocess_input(input_str)
    prediction = model.predict(input_array)[0]

    output_message = f'The predicted sales value is {prediction:.2f}'
    return render_template('index.html', prediction_text=output_message)
