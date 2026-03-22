import pickle
import pandas as pd

#import the ml model
with open('Model/model.pkl', 'rb') as f:
    model = pickle.load(f)

#ML Flow Version
MODEL_VERSION = '1.0.0'

def predict_premium(user_input: dict):
    
    input_df = pd.DataFrame([user_input])
    
    prediction =  model.predict(input_df)[0]
    
    return prediction
