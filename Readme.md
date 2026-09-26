Customer Purchase Prediction — Supervised Learning Mini-Task
A beginner-friendly machine learning project comparing Logistic Regression and Decision Tree classifiers to predict customer purchasing behavior based on Age and Annual Income.
---
📌 Project Overview
This project is part of a machine learning assignment designed to demonstrate how supervised learning algorithms work using Scikit-Learn. It takes a small tabular dataset, splits it into training and testing subsets, trains two distinct models, and evaluates their performance.
Features
Logistic Regression: A linear model that estimates the probability of a binary outcome.
Decision Tree Classifier: A tree-based model that makes predictions by splitting features into hierarchical conditional rules.
Model Evaluation: Compares the predictive accuracy of both algorithms on a test set.
---
📊 Dataset Structure
The dataset maps two independent features (`Age` and `Income`) to a binary target variable (`Purchased`).
Age	Income	Purchased ($0 = \text{No}, 1 = \text{Yes}$)
20	15000	0
22	18000	0
25	22000	0
28	30000	1
30	35000	1
32	40000	1
35	45000	1
38	50000	1
40	55000	1
45	60000	1
---
🛠️ Prerequisites & Installation
To run this Python script, you need to have Python installed along with the following libraries:
```bash
pip install pandas scikit-learn
```
---
🚀 How to Run the Code
Save the Python script (e.g., `app.py`) in your working directory.
Run the script using your terminal or IDE:
```bash
   python app.py
   ```
---
📝 Code Implementation
```python
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

# 5. Predict for a new customer
new_customer = pd.DataFrame([[17, 22000]], columns=['Age', 'Income'])
pred_log_reg = log_reg.predict(new_customer)
pred_dt = dt_clf.predict(new_customer)

print(f"Logistic Regression Prediction: {pred_log_reg[0]} (0 = No, 1 = Yes)")
print(f"Decision Tree Prediction: {pred_dt[0]} (0 = No, 1 = Yes)")

# 6. Evaluate Accuracy
acc_log_reg = accuracy_score(y_test, log_reg.predict(X_test))
acc_dt = accuracy_score(y_test, dt_clf.predict(X_test))

print(f"Logistic Regression Accuracy: {acc_log_reg * 100:.2f}%")
print(f"Decision Tree Accuracy: {acc_dt * 100:.2f}%")
```
---
💡 Key Learnings & Notes
Why 100% Accuracy? On tiny, completely clean, noise-free synthetic datasets, simple models easily isolate the decision boundary without error. Changing test sizes or adding noisy/overlapping data points will introduce real-world classification errors.