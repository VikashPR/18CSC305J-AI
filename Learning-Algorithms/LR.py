from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load the breast cancer dataset
cancer = load_breast_cancer()

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    cancer.data, cancer.target, test_size=0.2, random_state=42)

# Create a logistic regression model
lr_model = LogisticRegression()

# Train the model on the training data
lr_model.fit(X_train, y_train)

# Predict the target values for the test data
y_pred = lr_model.predict(X_test)

# Calculate the accuracy of the model
accuracy = lr_model.score(X_test, y_test)

# Print the accuracy as a percentage
print("Logistic Regression Accuracy: {:.2f}%".format(accuracy*100))
