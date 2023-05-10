from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# Load the breast cancer dataset
cancer = load_breast_cancer()

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    cancer.data, cancer.target, test_size=0.2, random_state=42)

# Create an SVM model
svm_model = SVC(kernel='linear')

# Train the model on the training data
svm_model.fit(X_train, y_train)

# Predict the target values for the test data
y_pred = svm_model.predict(X_test)

# Calculate the accuracy of the model
accuracy = svm_model.score(X_test, y_test)

# Print the accuracy as a percentage
print("SVM Accuracy: {:.2f}%".format(accuracy*100))
