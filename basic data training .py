from sklearn.linear_model import LinearRegression

# X = Input (feature)
X_train = [
    [1000],
    [1200],
    [1500],
    [1800]
]

# y = Output (target)
y_train = [
    200000,
    240000,
    300000,
    360000
]


# Create the model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# New house to predict
X_test = [
    [160]
]

# Predict price
y_pred = model.predict(X_test)

print(y_pred)