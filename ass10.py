# 1st cell: Import necessary libraries
import pandas as pd  # For data loading and manipulation
from sklearn.model_selection import train_test_split  # For splitting data into train and test sets
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, precision_score, recall_score  # Evaluation metrics
from sklearn.svm import SVC  # Support Vector Classifier for classification tasks

# 2nd cell: Load dataset
data = pd.read_csv("Assignment 10.csv")  # Load the dataset from CSV file

# 3rd cell: Drop unnecessary column
data = data.drop('Email No.', axis=1)  # Remove 'Email No.' column, which is not needed for modeling

# 4th cell: Separate features and target variable
X = data.drop('Prediction', axis=1)  # Features for model input (excluding the target column 'Prediction')
y = data['Prediction']  # Target variable indicating spam or not spam

# 5th cell:
X = data.drop('Prediction', axis=1)  # 'Prediction' is the target (spam/not spam)
y = data['Prediction']

# 6th cell: Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Use 80% of the data for training and 20% for testing, setting random_state for reproducibility

# 7th cell: Initialize and train the Support Vector Classifier (SVC) model
SVM = SVC(gamma='auto')  # Initialize SVC model with 'auto' gamma setting for simplicity
SVM.fit(X_train, y_train)  # Train the model on the training data

# 8th cell: Make predictions on the test set
y_pred = SVM.predict(X_test)  # Predict the target variable on the test data

# 9th cell: Calculate and store evaluation metrics
accuracy = accuracy_score(y_test, y_pred)  # Calculate accuracy of the model
precision = precision_score(y_test, y_pred)  # Calculate precision score
recall = recall_score(y_test, y_pred)  # Calculate recall score

# 10th cell: Print evaluation metrics for the model
print("Accuracy: ", accuracy)  # Print accuracy score
print("Precision: ", precision)  # Print precision score
print("Recall: ", recall)  # Print recall score

# 11th cell: Compute and display confusion matrix
cm = confusion_matrix(y_test, y_pred)  # Create confusion matrix to show true vs predicted labels
print("Confusion Matrix: ")
print(cm)  # Print confusion matrix to analyze model performance

# 12th cell: Generate and display classification report
print("Classification Report: ")
print(classification_report(y_test, y_pred))  # Detailed report showing precision, recall, f1-score, and support
