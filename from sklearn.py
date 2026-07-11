from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Load the dataset
iris = load_iris()

# Features and target
X = iris.data
y = iris.target

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=10
)

# Create the Naive Bayes model
model = GaussianNB()

# Train the model
model.fit(X_train, y_train)

# Predict test data
y_pred = model.predict(X_test)

# Print predicted values
print("Predicted Values:")
print(y_pred)

# Print actual values
print("\nActual Values:")
print(y_test)

# Find the accuracy
accuracy = accuracy_score(y_test, y_pred)
print("\nAccuracy:", accuracy)

# Predict a new flower
sample = [[5.0, 3.4, 1.5, 0.2]]
result = model.predict(sample)

print("\nPrediction Result:")
print("Class:", result[0])
print("Flower:", iris.target_names[result[0]])