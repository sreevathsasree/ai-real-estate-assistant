# AI Real Estate Assistant 🏠

A machine learning-powered web application for predicting real estate prices in Bangalore using Linear Regression.

## Features

- 🎯 Price prediction based on location, size, BHK, and bathrooms
- 🗺️ Covers 10 major locations in Bangalore
- 📊 Interactive Streamlit web interface
- 🤖 Machine learning model trained on realistic pricing data

## Locations Covered

- Whitefield
- Electronic City
- Hebbal
- Marathahalli
- Indiranagar
- Koramangala
- BTM Layout
- HSR Layout
- Jayanagar
- Rajaji Nagar

## Installation

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/ai-real-estate-assistant.git
cd ai-real-estate-assistant
```

2. Install required packages:
```bash
pip install -r Requirements.txt
```

3. Train the model:
```bash
python train_model.py
```

4. Run the application:
```bash
streamlit run app.py
```

## Project Structure

```
ai-real-estate-assistant/
│
├── app.py                 # Streamlit web application
├── train_model.py         # Model training script
├── Requirements.txt       # Project dependencies
├── model/                 # Model files (generated after training)
│   ├── price_model.pkl
│   ├── label_encoder.pkl
│   └── model_columns.json
└── README.md             # Project documentation
```

## Technologies Used

- **Python** - Programming language
- **Streamlit** - Web framework
- **scikit-learn** - Machine learning library
- **Pandas** - Data manipulation
- **NumPy** - Numerical computing

## How It Works

1. The model is trained on synthetic data with realistic pricing based on Bangalore real estate market
2. Features include: location, total square feet, number of bathrooms, and BHK
3. Linear Regression predicts property prices in lakhs (₹)
4. User inputs are processed through the trained model for instant predictions

## Usage

1. Select a location from the dropdown
2. Enter the total square footage
3. Choose number of bathrooms
4. Select BHK configuration
5. Click "Predict Price" to get the estimated price

## Contributing

Feel free to fork this project and submit pull requests for any improvements!

## License

This project is open source and available under the MIT License.
