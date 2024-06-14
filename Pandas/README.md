# Price Analysis and Prediction

This project aims to analyze iPhone prices across different versions and predict future prices using linear regression. The dataset used for this analysis is stored in a CSV file (`iphone_price.csv`).

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Example Output](#example-output)
- [Contributing](#contributing)
- [License](#license)
- [Credits](#credits)

## Overview

This project reads a CSV file containing iPhone prices for various versions, performs basic data analysis, and uses a linear regression model to predict future prices. It includes data visualization to illustrate the price trend across different iPhone versions.

## Features

- Reads and analyzes the iPhone price data from a CSV file.
- Displays the first few rows of the dataset and provides basic statistics.
- Checks for and handles missing values by filling them with 0.
- Adds a new column for discounted prices.
- Uses linear regression to predict future iPhone prices.
- Plots the price trend across different iPhone versions.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/basharul2002/iphone-price-analysis.git
   cd price-analysis

2. Install the required Python packages:
  ````sh
  pip install pandas matplotlib scikit-learn
  ````

## Usae

Place the  csv (Ex: iphone_price.csv) file in the same directory as the script.

Run the script:
```
python price_analysis.py
```


## Example Output
The script will output:

- First 5 rows of the dataframe.
- Basic information about the dataframe.
- Basic statistics of the dataframe.
- Missing values per column.
- First 5 rows after handling missing values and adding a discounted price column.
- Predicted prices for future iPhone versions (versions 15 to 30).
- A plot showing the price trend across different iPhone versions.
- Example of predicted prices output:

```
In Future predicted iPhone price:
Version   Predicted Price
15        1599.67
16        1699.45
17        1799.23
18        1899.01
...
```

Contributing
Contributions to this project are welcome! If you have any suggestions, improvements, or bug fixes, please submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

License
This project is licensed under the MIT License.

Credits
Developed and maintained by Basharul-Alam-Mazu



