# Immo-Eliza-api-deployment

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Contributors](#contributors)
- [Structure](#structure)
- [Timeline](#timeline)

## Description

This project provides a full-stack solution for predicting property prices in Belgium using a machine learning model deployed in a Streamlit app for predicting real estate prices in Belgium. The app allows users to input property details, such as the number of rooms, area, and location, to predict the estimated price of a property.
By leveraging a trained linear regression model, the app makes real-time price predictions.

## Installation

1. Clone the repository:https://github.com/elsagk/Immo-Eliza_api_deployment.git

2. Install Dependencies: Install the necessary libraries using pip:

   - pip install -r requirements.txt

   - Ensure that the requirements.txt file includes the following libraries:

   - streamlit

   - pandas

   - joblib

   - scikit-learn

3. Train the Model:

- Make sure the trained machine learning model (saved_model.pkl) is located in the model/ directory.

4. Run the Streamlit Application: To start the app, run:

- streamlit run app.py

- This will launch the web application in your default browser.

## Usage

- Input Data:

- The user provides input data through the web

- Prediction:

- After submitting the input, the app preprocesses the data and passes it to the trained machine learning model.

- The model predicts the price of the house based on the entered features.

- Output:

- The predicted price is displayed on the web page.

---Code Explanation:

- predict.py

- The predict.py file contains the predict() function, which loads a pre-trained model and predicts the house price based on the input data:

- cleaning_data.py:

- The preprocess() function in the cleaning_data.py file preprocesses the raw data by handling missing values and encoding categorical features:

- app.py:

- The Streamlit app allows users to input data and get real-time price predictions:

## Contributors

https://github.com/elsagk

## Structure

- Immo-Eliza-api-deployment/
- │
- ├── app.py # Streamlit app for user input and predictions
- ├── preprocessing/
- │ └── cleaning_data.py # Data preprocessing and cleaning
- ├── predict/
- │ └── prediction.py # Price prediction logic
- ├── model/
- │ └── saved_model.pkl # Pre-trained machine learning model
- └── README.md

## Timeline

- Duration: 5 days
- Deadline: 18/12/2024 17:00
