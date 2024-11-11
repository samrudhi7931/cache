# 1st cell: Import necessary libraries
import pandas as pd  # For data manipulation and analysis
import numpy as np  # For numerical computations
from sklearn.model_selection import train_test_split  # To split data into training and testing sets
from sklearn.linear_model import LinearRegression  # For linear regression model
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score  # Evaluation metrics
import matplotlib.pyplot as plt  # For plotting and visualizations
import seaborn as sns  # For statistical data visualization

# 2nd cell: Load and preview the dataset
df = pd.read_csv('Assignment 9.csv')  # Load dataset from CSV file into a DataFrame
print(df.head())  # Display the first few rows to understand the data structure

# 3rd cell: Check for missing values in each column
print(df.isnull().sum())  # Count missing values in each column to identify potential data cleaning needs

# 4th cell: Display column names in the dataset
print(df.columns)  # Print column names to understand features and identify the target column

# 5th cell: Separate features and target variable
X = df.drop(columns=['medv'])  # Select all columns except 'medv' (home prices) as features
y = df['medv']  # Set 'medv' column as the target variable

# 6th cell: Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Use 80% of data for training and 20% for testing, ensuring reproducibility with random_state

# 7th cell: Initialize and train the linear regression model
model = LinearRegression()  # Create an instance of the Linear Regression model
model.fit(X_train, y_train)  # Fit the model on the training data

# 8th cell: Make predictions on the test set
y_pred = model.predict(X_test)  # Predict home prices on the test set using the trained model

# 9th cell: Evaluate model performance using regression metrics
print("Model Evaluation Metrics:")
print(f"Mean Absolute Error: {mean_absolute_error(y_test, y_pred):.2f}")  # Calculate MAE
print(f"Mean Squared Error: {mean_squared_error(y_test, y_pred):.2f}")  # Calculate MSE
print(f"R^2 Score: {r2_score(y_test, y_pred):.2f}")  # Calculate R-squared for model accuracy

# 10th cell: Visualize actual vs predicted home prices with a scatter plot
plt.figure(figsize=(10, 6))  # Set plot size
sns.scatterplot(x=y_test, y=y_pred, alpha=0.7)  # Scatter plot of actual vs. predicted prices
plt.xlabel("Actual Prices")  # X-axis label
plt.ylabel("Predicted Prices")  # Y-axis label
plt.title("Actual vs Predicted Home Prices")  # Plot title
plt.show()  # Display the plot

# 11th cell: Visualize actual vs predicted prices with a regression line
plt.figure(figsize=(10, 6))  # Set plot size
sns.regplot(x=y_test, y=y_pred, scatter_kws={'alpha':0.7})  # Scatter plot with a regression line
plt.xlabel("Actual Prices")  # X-axis label
plt.ylabel("Predicted Prices")  # Y-axis label
plt.title("Actual vs Predicted Home Prices with Regression Line")  # Plot title
plt.show()  # Display the plot
