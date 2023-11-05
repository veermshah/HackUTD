import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle

# Load the data
data = pd.read_csv('data.csv')

print(data.columns)
"""
# Load the model
model = pickle.load(open('model.pkl', 'rb'))

# Preprocess the new data
new_data = [[1.0, 2.0, 3.0]]

# Make predictions on the new data
predictions = model.predict(new_data)

# Print the predictions
print(predictions)"""