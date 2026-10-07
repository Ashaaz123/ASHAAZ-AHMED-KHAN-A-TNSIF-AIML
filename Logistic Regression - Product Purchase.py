import numpy as np
from sklearn.linear_model import LogisticRegression

# Input data
# [Age, Income]
X = np.array([
    [20, 15000],
    [22, 18000],
    [25, 25000],
    [28, 30000],
    [30, 35000],
    [35, 40000],
    [40, 50000],
    [45, 60000]
])

# Output
y = np.array([0, 0, 0, 1, 1, 1, 1, 1])

# Create model
model = LogisticRegression()

# Train model
model.fit(X, y)

# Predict for a new customer
age = 32
income = 38000

prediction = model.predict([[age, income]])

if prediction[0] == 1:
    print("Purchased: Yes")
else:
    print("Purchased: No")