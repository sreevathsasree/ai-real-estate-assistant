import pandas as pd
import pickle
import json
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

print("🔄 Starting model training...")

# Create better synthetic data with proper pricing logic
np.random.seed(42)

locations = ['Whitefield', 'Electronic City', 'Hebbal', 'Marathahalli', 'Indiranagar', 
             'Koramangala', 'BTM Layout', 'HSR Layout', 'Jayanagar', 'Rajaji Nagar']

# Location price multipliers (per sqft base rate)
location_rates = {
    'Whitefield': 5500, 'Electronic City': 4500, 'Hebbal': 5000,
    'Marathahalli': 5200, 'Indiranagar': 7000, 'Koramangala': 6800,
    'BTM Layout': 5800, 'HSR Layout': 6200, 'Jayanagar': 6000,
    'Rajaji Nagar': 5300
}

n_samples = 1000
data = []

for _ in range(n_samples):
    location = np.random.choice(locations)
    bhk = np.random.randint(1, 6)
    bath = min(bhk, np.random.randint(1, bhk + 2))
    total_sqft = np.random.randint(600 + (bhk-1)*300, 1000 + (bhk-1)*500)
    
    # Realistic pricing: base_rate * sqft with some randomness
    base_rate = location_rates[location]
    price = (base_rate * total_sqft / 100000) * np.random.uniform(0.9, 1.1)
    
    data.append({
        'location': location,
        'total_sqft': total_sqft,
        'bath': bath,
        'bhk': bhk,
        'price': round(price, 2)
    })

df = pd.DataFrame(data)

print(f"✅ Created dataset with {len(df)} samples")
print(df.head())

# Encode location
le = LabelEncoder()
df['location_encoded'] = le.fit_transform(df['location'])

# Prepare features
X = df[['location_encoded', 'total_sqft', 'bath', 'bhk']]
y = df['price']

# Train simple fast model
model = LinearRegression()
model.fit(X, y)

print("✅ Model trained successfully")

# Save model
with open("model/price_model.pkl", "wb") as f:
    pickle.dump(model, f)

# Save label encoder
with open("model/label_encoder.pkl", "wb") as f:
    pickle.dump(le, f)

# Save feature info
feature_info = {
    'features': ['location_encoded', 'total_sqft', 'bath', 'bhk'],
    'locations': locations
}

with open("model/model_columns.json", "w") as f:
    json.dump(feature_info, f)

print("✅ Model + encoder saved successfully")

# Test predictions
test_location = 'Whitefield'
test_encoded = le.transform([test_location])[0]
test_input = [[test_encoded, 1200, 2, 2]]
test_price = model.predict(test_input)[0]

print(f"\n🧪 Test prediction:")
print(f"   Location: {test_location}")
print(f"   Config: 2 BHK, 1200 sqft")
print(f"   Predicted Price: ₹{test_price:.2f} Lakhs")