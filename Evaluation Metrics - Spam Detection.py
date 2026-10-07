from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Actual values
actual = [1, 1, 1, 0, 0, 0, 1, 0]

# Predicted values
predicted = [1, 1, 0, 0, 0, 1, 1, 0]

# Calculate metrics
accuracy = accuracy_score(actual, predicted)
precision = precision_score(actual, predicted)
recall = recall_score(actual, predicted)
f1 = f1_score(actual, predicted)

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1-Score:", f1)