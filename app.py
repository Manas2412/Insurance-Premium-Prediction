from fastapi import FastAPI
from fastapi.responses import JSONResponse
from Schema.user_input import User
from Model.predict import model, MODEL_VERSION, predict_premium
from Schema.prediction_presponse import PredictionResponse

app = FastAPI()

@app.get('/')
def home():
    return {"message": "Welcome to the Insurance Premium Prediction API. Use the /predict endpoint to get predictions."}

@app.get('/health')
def health_check():
    return {"status": "healthy", "model_version": MODEL_VERSION, 'model_loaded': model is not None}

@app.post("/predict", response_model=PredictionResponse)
def predict_premium(user: User):
    
    user_input = [{
        'bmi': user.bmi,
        'age_group': user.age_group,
        'lifestyle_risk': user.lifestyle_risk,
        'income_lpa': user.income_lpa,
        'occupation': user.occupation,
        'city_tier': user.city_tier
    }]
    
    try: 
        prediction =  predict_premium(user_input)
        return JSONResponse(content={"predicted_premium": prediction})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)