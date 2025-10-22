from flask import Flask, render_template, request
import pickle
import numpy as np
import os

app = Flask(__name__)

# Load the best model

model_path = os.path.join(os.path.dirname(__file__), 'best_netflix_model.pkl')

with open(model_path, "rb") as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get input values from form
        open_price = float(request.form["open"])
        high_price = float(request.form["high"])
        low_price = float(request.form["low"])
        volume = float(request.form["volume"])

        # Prepare data for model
        input_data = np.array([[open_price, high_price, low_price, volume]])

        # Predict
        predicted_close = model.predict(input_data)[0]
        predicted_close = round(predicted_close, 2)

        return render_template("index.html", 
                               prediction_text=f"📈 Predicted Close Price: ${predicted_close}")
    except Exception as e:
        return render_template("index.html", prediction_text=f"❌ Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
