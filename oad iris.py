import sys

try:
    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import accuracy_score
except ModuleNotFoundError:
    sys.exit(
        "scikit-learn is not installed. Install it with `pip install scikit-learn` and rerun this script."
    )


def main():
    # Load the Iris dataset
    iris = load_iris()

    # Store features and target
    X = iris.data
    y = iris.target

    # Split the dataset into training and testing data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Create the Logistic Regression model
    model = LogisticRegression(max_iter=200, solver="lbfgs", multi_class="auto")

    # Train the model
    model.fit(X_train, y_train)

    # Predict the test data
    predictions = model.predict(X_test)

    # Print predicted values
    print("Predicted Classes:")
    print(predictions)
    print("Predicted Names:")
    print([iris.target_names[label] for label in predictions])

    # Print actual values
    print("\nActual Classes:")
    print(y_test)
    print("Actual Names:")
    print([iris.target_names[label] for label in y_test])

    # Calculate accuracy
    accuracy = accuracy_score(y_test, predictions)
    print("\nAccuracy:", accuracy)

    # Predict a new flower
    new_flower = [[5.9, 3.0, 5.1, 1.8]]
    prediction = model.predict(new_flower)

    # Display the prediction
    print("\nNew Flower Prediction:")
    print("Class Number:", prediction[0])
    print("Flower Name:", iris.target_names[prediction[0]])


if __name__ == "__main__":
    main()