
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.metrics import classification_report, accuracy_score
from joblib import dump

# Load the CSV dataset
data = pd.read_csv("C:/Users/sejal/Desktop/PCOS_code1/PCOS.csv")
data = data.dropna()

# Feature Selection
x = data.drop(['PCOS (Y/N)'], axis=1)
y = data['PCOS (Y/N)']

# Normalize the dataset
scaler = MinMaxScaler(feature_range=(0, 1))
x_scaled = scaler.fit_transform(x)

# Reshape the input data for LSTM
x_reshaped = x_scaled.reshape((x_scaled.shape[0], 1, x_scaled.shape[1]))

# Split the dataset into training and test sets
x_train, x_test, y_train, y_test = train_test_split(x_reshaped, y, test_size=0.2, random_state=123)

# Build the LSTM model
model = Sequential()
model.add(LSTM(64, activation='relu', input_shape=(1, x_scaled.shape[1])))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=10, batch_size=16)

# Evaluate the model on the test set
y_pred = model.predict(x_test)
y_pred = [1 if pred > 0.5 else 0 for pred in y_pred]
accuracy = accuracy_score(y_test, y_pred)
classification_report = classification_report(y_test, y_pred)

print("Accuracy:", accuracy)
print("Classification Report:")
print(classification_report)

# Store the trained model in a joblib file
dump(model, "trained_model.joblib")
print("Trained model saved as 'trained_model.joblib'")
# Make predictions on new data
predictions = model.predict(x_reshaped)
predictions = [1 if pred > 0.5 else 0 for pred in predictions]

# Print the predictions
print("Predictions:", predictions)
