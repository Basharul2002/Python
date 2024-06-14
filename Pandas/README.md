# Price Analysis and Prediction

## Overview

This project performs price analysis and prediction using linear regression on product versions. The code reads a CSV file containing product prices and versions, performs basic data analysis, and predicts future prices using a linear regression model.

## Features

## Features

✨ **Data Reading and Analysis**: Reads and analyzes data from a CSV file.

📊 **Statistics Display**: Shows basic information and statistics about the data.

🔍 **Missing Values Handling**: Checks and fills missing values.

💰 **Discounted Prices Calculation**: Adds a new column with discounted prices.

📈 **Price Prediction**: Predicts future prices using linear regression.

📉 **Trend Plotting**: Plots the price trend for visualization.

## Requirements

- Python 3.x
- pandas
- matplotlib
- scikit-learn
- os (built-in)

## Installation

To get started, ensure you have Python installed on your system. Then, install the necessary packages:

```sh
pip install pandas matplotlib scikit-learn
```

## Usage
1. Clone the Repository
   ```sh
   git clone https://github.com/basharul2002/price-analysis-prediction.git
   cd price-analysis-prediction

2. Run the Script

Execute the script by running the following command:
```sh
python price_analysis_prediction.py
```

3. Follow the Prompts
   - Input your product name.
   - Enter the path to your CSV file.


## CSV File Format
Ensure your CSV file has the following format:

| version |	price |
|---------|-------|
|    1	 |  500  |
|    2	 |  550  |
|    3	 |  600  |
|   ...	 |  ...  |

## Example Output
   ```sh
   Input your product name: iPhone
   Enter your csv file path: path/to/your/file.csv

   First 5 rows of the dataframe:
      version  price
   0        1    500
   1        2    550
   2        3    600
   ...

   Dataframe info:
   <class 'pandas.core.frame.DataFrame'>
   RangeIndex: ... entries, 0 to ...
   Data columns (total 2 columns):
    #   Column   Non-Null Count  Dtype
   ---  ------   --------------  -----
    0   version  ... non-null    int64
    1   price    ... non-null    float64
   ...

   Basic statistics:
            version  price
   count   ...       ...
   mean    ...       ...
   std     ...       ...
   min     ...       ...
   25%     ...       ...
   50%     ...       ...
   75%     ...       ...
   max     ...       ...

   Missing values per column:
   version    0
   price      0

   First 5 rows after modification:
      version  price  Discounted_Price
   0        1    500             450.0
   1        2    550             495.0
   2        3    600             540.0
   ...

   In Future predicted iphone price:
   Version   Predicted Price
      15        ...
      16        ...
      17        ...
      ...
```
## Contributing
Contributions are welcome! If you have any ideas or improvements, feel free to fork the repository and submit a pull request.

## License
This project is licensed under the MIT License.

## Credits
Developed and maintained by [Basharul-Alam-Mazu](www.github.com/basharul2002)

Enjoy exploring and using this project to analyze and predict prices!
```sh
Feel free to adjust the content and formatting to better suit your needs.
