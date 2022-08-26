# Equity Analysis Tool Application & Analysis Report

## Project Executive Summary (Visit AppToAnalysisUpdate Branch for the Latest and Greatest Code)

To provide our clients with an investment recommendation that will reduce the overall risk of their portfolio while enhancing their cumulative returns.

This program analyzes a users current stock holdings and compares them to a selected group of large sector ETFs and crypto equities. It then gives them recommendations for which ETFs or crypto assets they should add to their portfolio. The program starts by running in a CLI and asks the user to input their current stocks tickers and how many shares they have of each. It then outputs and saves the data into a CSV. The user will then open Jupyter Lab and load that CSV data into a Juypter Notebook file. After the data is loaded, the program runs through the ETFs and compares the values of them to the values of the user's current portfolio. It finishes by offering recommendations for additional equities they can add to strengthen their portfolio.

---

## Technologies

This application is compatible with Python 3.9. The Pandas, numpy, matplotlib, os, json, requests, pathlib, dontenv as well as the alpaca trade api, matplotlib and altair libraries and dependencies are all used in the program.

Pandas is used for data science and analysis and machine learning. Pathlib allows the import of files, in this case CSV data. Numpy is a package that allows for scientific computing and array handling. Matplotlib allows for the visualization of data in the form of plots and graphs. The Alpaca Trade Api allows access to the exchange data from Alpaca. Altair is a declarative statistical visualization library for Python.

Documentation for the Pandas library can be found [here.](https://pandas.pydata.org/docs/)

Documentation for the Numpy library can be found [here.](https://numpy.org/doc/1.23/user/index.html)

Documentation for matplotlib can be found [here.](https://matplotlib.org/stable/users/index)

Documentation for the Alpaca Trade Api can be found [here.](https://pypi.org/project/alpaca-trade-api/)

Documentation for the Altair can be found [here.](https://altair-viz.github.io/getting_started/overview.html)

Documentation for JSON can be found [here.](https://docs.python.org/3/library/json.html)

Documentation for pathlib can be found [here.](https://docs.python.org/3/library/pathlib.html)

Documentation for dotenv can be found [here.](https://pypi.org/project/python-dotenv/)

Documentation for os can be found [here.](https://docs.python.org/3/library/os.html)

---

## Installation Guide

Download and install Anaconda to your local machine [here.](https://www.anaconda.com)
Download and install Jupyter Lab [here.](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html)

Install the following dependencies before running the program.

To install the pathlib, pandas, numpy, altair, alpaca trade api and matplotlib libraries type the following into your CLI:

```
$ python
$ pip install pathlib
$ pip install pandas
$ pip install numpy
$ pip install -U matplotlib
$ pip3 install alpaca-trade-api
$ pip install altair vega_datasets
$ pip install python-dotenv
```

Clone the Equity-Analysis-Tool main branch repository to your local machine.

Sign up for a free Alpaca trading account at https://app.alpaca.markets/login 
From here you will be able to create your API Keys.

---

## Usage

Configure your personal .env file as below (This file will be hidden so you may have to enable "show hidden files" on your machine to view it).
```
ALPACA_API_KEY = "API Key Goes Here" 
ALAPACA_API_SECRET_KEY = "API Secret Key Goes Here"
```
Go to your local machine's CLI or Terminal and navigate to the Equity-Analysis-Tool directory.

Activate your Conda Development Environment in your CLI or terminal.
```
$ conda activate dev
```
Run the app.py file to start the Equity-Analysis-Tool Client application.
```
$ python app.py
```

### Using the Equity Analysis Tool CLI Application

After the app.py application has been executed, the client will be prompted for the tickers of their portfolio holdings and quantity of shares of each.

Proceed through the application instructions until the application is complete. The program will finish by exporting your data to a .csv file which will be stored in the "resources" directory.

Check the "resources" folder in the Equity-Analysis-Tool to confirm your .csv file has been successfully created

### Using the Equity Analysis Tool Jupyter Lab Notebook

After completion of the Equity Analysis Tool application, you will navigate to the StockAnalysisReport.ipynb under the ClientConfidentials folder.

Launch Jupyter Lab from the CLI or Terminal.
```
$ jupyter lab
```
*This will open a web page on your localhost machine with the notebook

Run each of the Jupyter Notebook cells in sequence from top to bottom following the instructions to review the your Client Ticker & ETF Risk and Return Analysis Report.


---

## Contributors

Developed by:

Tanner Franklin
Email: tannerdfranklin@gmail.com

Tyler Hillison
Email: thillison@gmail.com

Graham Johnstone
Email: johnstonegr@gmail.com

---

## License
This code is published under the Creative Commons License, 2022.

