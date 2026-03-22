from fastapi import FastAPI
from fastapi.responses import JSONResponse
from Schema.user_input import User
from Model.predict import model, MODEL_VERSION, predict_premium

app = FastAPI()

@app.get('/')
def home():
    return {"message": "Welcome to the Insurance Premium Prediction API. Use the /predict endpoint to get predictions."}

@app.get('/health')
def health_check():
    return {"status": "healthy", "model_version": MODEL_VERSION, 'model_loaded': model is not None}

@app.post("/predict")
def predict_premium(user: User):
    
    user_input = [{
        'bmi': user.bmi,
        'age_group': user.age_group,
        'lifestyle_risk': user.lifestyle_risk,
        'income_lpa': user.income_lpa,
        'occupation': user.occupation,
        'city_tier': user.city_tier
    }]
    
    prediction =  predict_premium(user_input)
    
    return JSONResponse(content={"predicted_premium": prediction})