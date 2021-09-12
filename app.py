import json
import pickle
from flask import Flask, request
from process_input import process_input
import numpy as np


# DEFINING PATH TO THE SAVED MODEL'S .pkl FILE
SAVED_MODEL_PATH = "classifier.pkl"

# LOADING THE CLASSIFIER FROM FILE
classifier = pickle.load(open(SAVED_MODEL_PATH, "rb"))

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home() -> str:
    """
    Homepage for this API.
    :return: Basic info about the API. A short introductory message
    """
    return ("""Welcome to Funmi Somoye's house price prediction API. This API has only one useful endpoint \n
              Predict House prices via the endpoint using a POST request.\n 
              Inputs should be a list of 13 numbers"""), 200


# CREATING ROUTE FOR MODEL PREDICTION
@app.route("/predict", methods=['POST'])
def predict() -> str:
    """
    Predicts the prices of houses using the trained model based on the inputs passed in the request.
    :return: predicted class for the request
    """
    try:
        input_params = process_input(request.data)
        predictions = classifier.predict(input_params)
        return json.dumps({"predicted_class": predictions.tolist()})
    except (KeyError, json.JSONDecodeError, AssertionError):
        return json.dumps({"error": "CHECK INPUT"}), 400
    except:
        return json.dumps({"error": "PREDICTION FAILED"}), 500