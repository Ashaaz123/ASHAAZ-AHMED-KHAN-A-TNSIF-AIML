from sklearn.tree import DecisionTreeClassifier

# Weather:
# Sunny = 0
# Rainy = 1
# Cloudy = 2

# Temperature:
# Hot = 0
# Cool = 1

X = [
    [0, 0],   # Sunny Hot
    [0, 1],   # Sunny Cool
    [1, 1],   # Rainy Cool
    [1, 0],   # Rainy Hot
    [2, 0],   # Cloudy Hot
    [2, 1],   # Cloudy Cool
    [0, 0],   # Sunny Hot
    [1, 1]    # Rainy Cool
]

# Play output
y = [0, 1, 1, 0, 1, 1, 0, 1]

# Create model
model = DecisionTreeClassifier(random_state=42)

# Train model
model.fit(X, y)

# Prediction
# Example: Sunny + Cool
prediction = model.predict([[0, 1]])

if prediction[0] == 1:
    print("Play: Yes")
else:
    print("Play: No")