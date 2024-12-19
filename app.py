from flask import Flask, render_template, request
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

app = Flask(__name__)

# Load your dataset
data = pd.read_csv("Historic_sorted.csv")
years = list(range(2021, 2026))
months = ['JUN', 'JUL', 'AUG', 'SEP']

# Train ARIMA models for each month and make predictions
predictions = {}
for month in months:
    train = data[month].iloc[:-5]
    model = ARIMA(train, order=(5, 1, 0))
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=5)
    predictions[month] = list(forecast)

# Convert predictions to a DataFrame
predicted_df = pd.DataFrame(predictions)
predicted_df['YEAR'] = years

# Function to evaluate hazard levels based on precipitation
def evaluate_hazard_level(value):
    if value > 185:  # Hazardous
        return "Hazardous"
    elif 100 <= value <= 185:  # Moderate
        return "Moderate"
    else:  # Low
        return "Low"

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    hazard_level = None

    if request.method == 'POST':
        selected_year = int(request.form['year'])
        selected_month = request.form['month']

        # Find prediction for the specified year and month
        month_abbr = selected_month[:3].upper()
        prediction_row = predicted_df[predicted_df['YEAR'] == selected_year]
        if not prediction_row.empty:
            predicted_value = prediction_row.iloc[0][month_abbr]
            hazard_level = evaluate_hazard_level(predicted_value)
            result = {
                "Year": selected_year,
                "Month": selected_month,
                "Prediction": round(predicted_value, 2),
                "Hazard_Level": hazard_level,
            }

    return render_template("index.html", result=result)

if __name__ == '__main__':
    app.run(debug=True)
