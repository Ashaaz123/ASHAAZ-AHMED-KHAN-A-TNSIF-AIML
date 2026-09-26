import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# 1. Create the dataset
data = {
    'Age': [20, 22, 25, 28, 30, 32, 35, 38, 40, 45],
    'Income': [15000, 18000, 22000, 30000, 35000, 40000, 45000, 50000, 55000, 60000],
    'Purchased': [0, 0, 0, 1, 1, 1, 1, 1, 1, 1]
}
df = pd.DataFrame(data)

# Features and Target
X = df[['Age', 'Income']]
y = df['Purchased']

# 2. Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Train Logistic Regression
log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)

# 4. Train Decision Tree
dt_clf = DecisionTreeClassifier(random_state=42)
dt_clf.fit(X_train, y_train)

# 5. Predict for a new customer (Age = 27, Income = 28000)
new_customer = pd.DataFrame([[27, 28000]], columns=['Age', 'Income'])
pred_log_reg = log_reg.predict(new_customer)
pred_dt = dt_clf.predict(new_customer)

print(f"Logistic Regression Prediction: {pred_log_reg[0]} (0 = No, 1 = Yes)")
print(f"Decision Tree Prediction: {pred_dt[0]} (0 = No, 1 = Yes)")

# 6. Evaluate Accuracy
acc_log_reg = accuracy_score(y_test, log_reg.predict(X_test))
acc_dt = accuracy_score(y_test, dt_clf.predict(X_test))

print(f"Logistic Regression Accuracy: {acc_log_reg * 100:.2f}%")
print(f"Decision Tree Accuracy: {acc_dt * 100:.2f}%")