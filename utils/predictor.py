import pickle
import json

# Load once at startup
with open("model/price_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("model/label_encoder.pkl", "rb") as f:
    label_encoder = pickle.load(f)

with open("model/model_columns.json", "r") as f:
    feature_info = json.load(f)

def predict_price(location, sqft, bhk, bath):
    try:
        # Encode location
        location_encoded = label_encoder.transform([location])[0]
        
        # Create input [location_encoded, total_sqft, bath, bhk]
        input_data = [[location_encoded, sqft, bath, bhk]]
        
        # Predict
        price = model.predict(input_data)[0]
        
        return round(price, 2)
    
    except Exception as e:
        print(f"Prediction error: {e}")
        return 75.0  # fallback