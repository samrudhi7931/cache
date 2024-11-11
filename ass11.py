# 1st cell: Import necessary libraries
import pandas as pd  # For data manipulation and analysis
import numpy as np  # For numerical operations
import matplotlib.pyplot as plt  # For data visualization
from sklearn.cluster import KMeans  # For performing K-Means clustering

# 2nd cell: Load dataset and display the first few rows
df = pd.read_csv("Assignment 11.csv", encoding='latin')  # Load dataset, specifying encoding for compatibility
print(df.head())  # Display the first 5 rows of the dataset to preview the data

# 3rd cell: Check data types of each column
print(df.dtypes)  # Print data types to understand feature formats and identify any necessary conversions

# 4th cell: Select features for clustering
X = df.iloc[:, [3, 4]].values  # Select specific columns (at index positions 3 and 4) as feature set for clustering

# 5th cell: Initialize an empty list to store Within-Cluster Sum of Squares (WCSS)
wcss = []  # WCSS will be calculated for each K value and used in the elbow method

# 6th cell: Apply K-Means for different K values to calculate WCSS
for i in range(1, 11):  # Loop through values of K from 1 to 10
    kmeans = KMeans(n_clusters=i, init="k-means++", random_state=42)  # Initialize KMeans with current K value
    kmeans.fit(X)  # Fit K-Means on the selected feature set
    wcss.append(kmeans.inertia_)  # Append WCSS for the current K value to the list

# 7th cell: Plot the elbow method to determine optimal K
ks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Define range of K values
plt.plot(ks, wcss, 'bx-')  # Plot WCSS against K values
plt.title("Elbow Method")  # Title for the plot
plt.xlabel("K value")  # Label for x-axis
plt.ylabel("WCSS")  # Label for y-axis (Within-Cluster Sum of Squares)
plt.show()  # Display the plot to visualize the "elbow"

# 8th cell: Display summary statistics of the dataset
print(df.describe())  # Show descriptive statistics to understand data distribution and detect potential scaling needs

# 9th cell: Scale the feature set using StandardScaler
from sklearn.preprocessing import StandardScaler  # Import StandardScaler for feature scaling
ss = StandardScaler()  # Initialize scaler
scaled = ss.fit_transform(X)  # Scale the selected features to standardize the data

# 10th cell: Calculate WCSS for scaled data using different K values
wcss = []  # Reset WCSS list for scaled data
for i in range(1, 11):  # Loop through K values from 1 to 10
    clustering = KMeans(n_clusters=i, init="k-means++", random_state=42)  # Initialize KMeans with current K
    clustering.fit(scaled)  # Fit K-Means on the scaled feature set
    wcss.append(clustering.inertia_)  # Append WCSS for scaled data

# 11th cell: Plot the elbow method for scaled data to determine optimal K
plt.plot(ks, wcss, 'bx-')  # Plot WCSS against K values for scaled data
plt.title("Elbow Method (Scaled Data)")  # Title for the plot indicating scaled data
plt.xlabel("K value")  # Label for x-axis
plt.ylabel("WCSS")  # Label for y-axis (Within-Cluster Sum of Squares)
plt.show()  # Display the plot
