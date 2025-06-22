# 🏡 House Price Prediction Web App

This is a Flask-based web application that predicts house prices using a trained **Linear Regression model**. The model is trained on a dataset with features like square footage, bedrooms, bathrooms, location, and more.

---

## 🔧 Features

- Input house details via a web form
- Predict house price using a trained ML model
- Uses a Linear Regression pipeline with OneHotEncoding for categorical features
- Styled with HTML/CSS
- Model is saved and loaded using `joblib`

---

```bash
House-Price-Prediction/
│
├── app.py                        # Flask application
├── train_model.py               # Script to train and save the model
├── data.csv                     # Dataset used for training
├── linear_regression_model.pkl  # Saved ML model
├── README.md                    # Project info
├── static/
│   └── style.css                # CSS styling
└── templates/
    └── index.html               # Web page UI
