# Pairs Trading
This includes a notebook on how to implement Quantitative Strategies, specifically the Pairs Trading Algorithm.



It involves the following:

* **1**: Creating a model that test for stationarity.
* **2**: Creating a model that test for cointegration.
* **3**: Assigning a portfolio of assests and testing for a cointegrated pair among the dataset.
* **4**: Establishing features and labels that will allow us to create trading signals for the strategy.

## Data

I used the data from [Yahoo Finance](https://finance.yahoo.com/), which provides historical financial data for free. This data was extracted via the [yFinance](https://pypi.org/project/yfinance/) Python module.

## Enviroment and Tools

The following are the modules we will use in this notebook. However, the program relies on many more dependencies than what is shown here. Please be sure to set up a virtual enviroment and install the ```requirements.txt``` file before running this programming on your own.

1. Jupyter NoteBook
2. Numpy
3. Pandas
4. Matplotlib
5. Seaborn
6. Statsmodels
7. Pandas DataReader
8. DateTime
9. yFinance (formally known as `Fix Yahoo Finance`)