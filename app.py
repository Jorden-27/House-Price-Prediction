from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load("House Price Prediction/linear_regression_model.pkl")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    data = {
        'bedrooms': float(request.form['bedrooms']),
        'bathrooms': float(request.form['bathrooms']),
        'sqft_living': int(request.form['sqft_living']),
        'sqft_lot': int(request.form['sqft_lot']),
        'floors': float(request.form['floors']),
        'waterfront': int(request.form['waterfront']),
        'view': int(request.form['view']),
        'condition': int(request.form['condition']),
        'sqft_above': int(request.form['sqft_above']),
        'sqft_basement': int(request.form['sqft_basement']),
        'yr_built': int(request.form['yr_built']),
        'yr_renovated': int(request.form['yr_renovated']),
        'city': request.form['city'],
        'statezip': request.form['statezip'],
    }
    
    input_df = pd.DataFrame([data])
    prediction = model.predict(input_df)[0]

    return render_template("index.html", prediction_text=f"Predicted Price: ${prediction:,.2f}")

if __name__ == '__main__':
    app.run(debug=True)
