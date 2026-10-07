import numpy as np
from sklearn.linear_model import LinearRegression

# Input data
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8]])

# Output data
y = np.array([20000, 25000, 30000, 35000, 40000, 45000, 50000, 55000])

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Predict salary for 5 years of experience
prediction = model.predict([[5]])

print("Predicted Salary:", prediction[0])