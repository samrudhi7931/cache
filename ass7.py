# 1st cell:
#  Import necessary libraries
import pandas as pd  # For data manipulation and analysis
import numpy as np  # For numerical operations
from sklearn.preprocessing import MinMaxScaler  # For scaling data to a specific range

# 2nd cell: 
# Load the dataset and display the first few rows
df = pd.read_csv('Assignment 7.csv')  # Load data from a CSV file into a DataFrame
df.head()  # Display the first few rows of the DataFrame to get an overview of the data

# 3rd cell:
#  Display dataset structure and summary statistics
df.info()  # Show data types and non-null values for each column
df.describe()  # Show summary statistics for numeric columns in the dataset

# 4th cell:
#  Check for and handle missing values
df.isnull().sum()  # Count the number of missing values in each column
df['Age'] = df['Age'].fillna(df['Age'].mean())  # Fill missing 'Age' values with the column mean
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])  # Fill missing 'Embarked' values with the most frequent value (mode)

# 5th cell: Detect and print outliers, scale numerical columns, and encode categorical columns

# Select only numerical columns for processing
numerical_cols = df.select_dtypes(include=np.number).columns

# Loop through each numerical column to detect outliers using the IQR method
for col in numerical_cols:
    Q1 = df[col].quantile(0.25)  # Calculate the first quartile (Q1) for the column
    Q3 = df[col].quantile(0.75)  # Calculate the third quartile (Q3) for the column
    
    # Calculate IQR and identify outliers for the current column
    IQR = Q3 - Q1
    lowerBound = Q1 - 1.5 * IQR  # Define lower boundary for outliers
    upperBound = Q3 + 1.5 * IQR  # Define upper boundary for outliers
    
    # Filter rows in the DataFrame that are outliers in this column
    outliers = df[(df[col] < lowerBound) | (df[col] > upperBound)]
    
    # If outliers are present, print them
    if not outliers.empty:
        print(f"Outliers in '{col}': ")
        print(outliers[[col]])
        print("\n")

# Scale 'Age' and 'Fare' columns to a 0-1 range
scaler = MinMaxScaler()
df[['Age', 'Fare']] = scaler.fit_transform(df[['Age', 'Fare']])
df.head()  # Display the first few rows of the DataFrame after scaling

# Convert categorical columns ('Sex' and 'Embarked') into dummy/indicator variables
df = pd.get_dummies(df, columns=['Sex', 'Embarked'], dtype=int)
df.head()  # Display the first few rows of the DataFrame after encoding
