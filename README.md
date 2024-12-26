
# Precipitation Prediction for Construction Businesses

This Project is develooped as part of the 8-hour National Level Hackathon [VertechX-12.0](https://vertechx.mvjce.edu.in) by, MVJ College of Engineering.

## Description:
This project focuses on predicting precipitation for the construction industry for the next 1-2 years(specific monsoon months) using historical data and machine learning techniques under the Theme-"Disaster Preparedness and Emergency Response.

### Dataset: 
The project utilizes a CSV file named "Historic_dataset.csv" containing historical precipitation data for past 20 years and monsoon months. As the dataset is consistent across all feratures and normal, no pre-processing techniques have been applied.

### Model Training and Predictions:

- The code employs the ARIMA (Autoregressive Integrated Moving Average) model for time series forecasting.
- It trains the model on historical data for specific months (June, July, August, September, and June-September combined).
- The trained model then predicts precipitation for the next five years (2021-2025) based on the chosen month.
- Evaluation Metrics for the year 2022:
  
![image](https://github.com/user-attachments/assets/0cabf10b-7cbf-43de-9f24-5e80dbb02e5a)

![037b50f9-9990-4c57-bdc8-322b007ae69e](https://github.com/user-attachments/assets/a10a3dd2-2232-4ff7-8b40-16294339969b)

### Tech Stack
#### Languages: Python, HTML/CSS.
#### Technologies/Frameworks: Machine Learning--ARIMA, Flask, Data Analytics

### Challenges
- Weather prediction is inherently complex and subject to various factors.
- The accuracy of predictions can be limited by the quality and historical range of the data used to train the model.
- External factors like climate change can also introduce uncertainty into the predictions.
- Unavailability and inaccessable to the real time data.

### Conclusions
Predicted the precipitation for the given years for specific months respectively.

