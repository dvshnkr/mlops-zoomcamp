import pickle
from flask import Flask, request, jsonify
import pandas as pd

app = Flask("duration-prediction")


def load_model(model_path="lin_reg.bin"):
    with open(model_path, "rb") as f_in:
        return pickle.load(f_in)

def predict(X):
    model = load_model()
    preds = model.predict(X)
    return preds[0][0]


@app.route('/predict', methods=['POST'])
def prediction_endpoint():
    ride = request.get_json()

    # since the dictionary values are not lists / collections, passing an index is required
    X = pd.DataFrame(ride, index=[0]) 

    pred = predict(X)

    result =  {
        # ride is a `dict` object as soon as a json object is received
        # "type": str(type(ride)), 
        "duration": pred
    }

    return jsonify(result)


if __name__=="__main__":
    app.run(debug=True, host='127.0.0.1', port=9696)

