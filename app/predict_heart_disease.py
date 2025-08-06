# predict_heart_disease.py

import pickle
import numpy as np

def load_model(path=r'models\xgb_heart_model_final.pkl'):
    with open(path, 'rb') as file:
        return pickle.load(file)

def predict(features_dict):
    model = load_model()
    features = np.array([list(features_dict.values())])
    prediction = model.predict(features)[0]
    return int(prediction)
