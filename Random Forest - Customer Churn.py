from sklearn.ensemble import RandomForestClassifier

# Input data
# [Age, Tenure, Monthly Bill]

X = [
    [22, 2, 500],
    [25, 5, 600],
    [30, 1, 800],
    [35, 8, 550],
    [40, 10, 500],
    [28, 3, 900],
    [45, 12, 650],
    [32, 2, 850]
]

# Churn output
y = [1, 0, 1, 0, 0, 1, 0, 1]

# Create Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train model
model.fit(X, y)

# Predict for a new customer
age = 30
tenure = 4
monthly_bill = 700

prediction = model.predict([[age, tenure, monthly_bill]])

if prediction[0] == 1:
    print("Churn: Yes - Customer may leave")
else:
    print("Churn: No - Customer may stay")