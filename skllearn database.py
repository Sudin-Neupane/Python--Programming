import sys

try:
    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.metrics import accuracy_score
except ModuleNotFoundError as exc:
    sys.exit(
        "scikit-learn is not installed. Install it with `pip install scikit-learn` and rerun this script."
    )


def main():
    # Load the Iris dataset
    iris = load_iris()

    # Store features and labels
    X = iris.data
    y = iris.target

    # Split the dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=1
    )

    # Create KNN model
    model = KNeighborsClassifier(n_neighbors=3)

    # Train the model
    model.fit(X_train, y_train)

    # Test the model
    predictions = model.predict(X_test)

    # Display predictions
    print("Predicted labels:")
    print(predictions)
    print("Predicted names:")
    print([iris.target_names[label] for label in predictions])

    # Display actual labels
    print("\nActual labels:")
    print(y_test)
    print("Actual names:")
    print([iris.target_names[label] for label in y_test])

    # Calculate accuracy
    accuracy = accuracy_score(y_test, predictions)
    print("\nAccuracy:", accuracy)

    # Predict a new flower
    new_flower = [[6.1, 2.8, 4.7, 1.2]]
    result = model.predict(new_flower)

    print("\nNew flower prediction:")
    print(iris.target_names[result[0]])


if __name__ == "__main__":
    main()