import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import os

# Prodct name
productName = input('Input your product name: ')

# Define the file path
file_path = input('Enter your csv file path: ')

# Check if the file exists at the given path
if os.path.exists(file_path):
    # Read the CSV file
    data = pd.read_csv(file_path)

    # Display the first few rows
    print("First 5 rows of the dataframe:")
    print(data.head())
    
    # Display basic information about the dataframe
    print("\n\nDataframe info:")
    print(data.info())
    
    # Display basic statistics
    print("\n\nBasic statistics:")
    print(data.describe())
    
    # Check for missing values
    print("\n\nMissing values per column:")
    print(data.isnull().sum())
    
    # Fill missing values with 0
    data_filled = data.fillna(0)
    
    # Add a new column with discounted prices
    data_filled['Discounted_Price'] = data_filled['price'] * 0.9
    
    # Display the first few rows of the modified dataframe
    print("\n\nFirst 5 rows after modification:")
    print(data_filled.head())

   
    # Linear Regression Model
    print(f'\n\nIn Future predicted {productName.lower()} price:')
    model = LinearRegression()
    model.fit(data[['version']].values, data[['price']])

    print('Version   Predicted Price')
    for i in range(15, 30):
        predicted_price = model.predict([[i]])
        print(f'{i}        {predicted_price[0][0]:.2f}')  # Accessing the predicted price correctly

    # Plot the data
    plt.plot(data_filled['version'], data_filled['price'], marker='o', linestyle='-', color='b')
    plt.xlabel(f'{productName} Version')
    plt.ylabel('Price')
    plt.title(f'{productName} Price by Version')
    plt.grid(True)
    plt.show()

else:
    print(f"Error: The file '{file_path}' does not exist.")
