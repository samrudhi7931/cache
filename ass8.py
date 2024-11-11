# 1st cell: Import necessary libraries
import numpy as np  # For numerical operations
import pandas as pd  # For data manipulation and analysis
import matplotlib.pyplot as plt  # For plotting and visualizations
import seaborn as sns  # For statistical data visualization
from sklearn.model_selection import StratifiedKFold, cross_val_score  # For stratified K-fold cross-validation
from sklearn.linear_model import LogisticRegression  # Logistic Regression model
from sklearn.tree import DecisionTreeClassifier  # Decision Tree model
from sklearn.ensemble import RandomForestClassifier  # Random Forest model
from sklearn.neighbors import KNeighborsClassifier  # K-Nearest Neighbors model
from sklearn.naive_bayes import GaussianNB  # Gaussian Naive Bayes model

# 2nd cell: Load and preview the dataset
penguins_data = pd.read_csv('Assignment 8.csv')  # Load penguins dataset from CSV file
penguins_data.head()  # Display the first few rows of the dataset to understand its structure

# 3rd cell: Initial data exploration
penguins_data.info()  # Display data types and non-null counts for each column
penguins_data.species.value_counts()  # Show the count of each species category in the dataset
penguins_data.isnull().sum()  # Check for missing values in each column

# 4th cell: Handle missing values, visualize data, and encode categorical variables

# Fill missing values in float columns with the mean of each column
for column_name in penguins_data.select_dtypes(include='float', exclude='object'):
    penguins_data[column_name] = penguins_data[column_name].fillna(penguins_data[column_name].mean())

# Fill missing values in the 'sex' column using forward fill
penguins_data['sex'] = penguins_data['sex'].ffill()

# Visualize species distribution by bill length and depth using a scatter plot
sns.scatterplot(x='bill_length_mm', y='bill_depth_mm', hue='species', data=penguins_data, style='species')

# Encode categorical columns 'sex' and 'island' using label encoding
from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
for col in ['sex', 'island']:
    penguins_data[col] = label_encoder.fit_transform(penguins_data[col])

# Standardize numerical columns to improve model performance
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
for col in ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']:
    penguins_data[col] = scaler.fit_transform(penguins_data[[col]])

# 5th cell: Perform Principal Component Analysis (PCA) for dimensionality reduction
from sklearn.decomposition import PCA

# Separate features and target variable
X = penguins_data.drop('species', axis=1)  # Features
Y = penguins_data['species']  # Target variable

# Apply PCA to reduce features to 3 principal components
PCA_TR = PCA(n_components=3)
X_train = PCA_TR.fit_transform(X)  # Transform features with PCA

# Display the variance explained by each principal component
PCA_TR.explained_variance_ratio_

# Display PCA components for each feature
pd.DataFrame(PCA_TR.components_, columns=X.columns, index=['PC-1', 'PC-2', 'PC-3'])

# 6th cell: Initialize classifiers and evaluate models using Stratified K-Fold cross-validation
LRM = LogisticRegression()  # Logistic Regression model
DTC = DecisionTreeClassifier()  # Decision Tree model
RFC = RandomForestClassifier()  # Random Forest model
KNC = KNeighborsClassifier()  # K-Nearest Neighbors model
NBC = GaussianNB()  # Gaussian Naive Bayes model

# Define Stratified K-Fold cross-validator
SKF = StratifiedKFold(n_splits=10, shuffle=True, random_state=10)

# Calculate and print the cross-validation accuracy scores for each model
print(f'LogisticRegression : {round(cross_val_score(LRM, X_train, Y, cv=SKF, scoring="accuracy").mean() * 100, 2)}%')
print(f'DecisionTreeClassifier : {round(cross_val_score(DTC, X_train, Y, cv=SKF, scoring="accuracy").mean() * 100, 2)}%')
print(f'RandomForestClassifier : {round(cross_val_score(RFC, X_train, Y, cv=SKF, scoring="accuracy").mean() * 100, 2)}%')
print(f'KNeighborsClassifier : {round(cross_val_score(KNC, X_train, Y, cv=SKF, scoring="accuracy").mean() * 100, 2)}%')
print(f'GaussianNB : {round(cross_val_score(NBC, X_train, Y, cv=SKF, scoring="accuracy").mean() * 100, 2)}%')
