import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle

"""
# Load the data
data = pd.read_csv('data.csv')

X = data[['ltv', 'dti', 'fedti']]
y = data['eligibility']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create and train the logistic regression model
model = LogisticRegression(solver='liblinear', max_iter=100)
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Evaluate the model's performance
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)

# Save the model
pickle.dump(model, open('model.pkl', 'wb'))
"""

def predict(ltv, dti, fedti):
    # Load the model
    model = pickle.load(open('model.pkl', 'rb'))

    # Preprocess the new data
    new_data = pd.DataFrame([[ltv, dti, fedti]], columns=['ltv', 'dti', 'fedti'])

    # Make predictions on the new data
    predictions = model.predict(new_data)

    return predictions

print(predict(60, 43, 28))