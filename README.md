# Equity Analysis Tool Application & Analysis Report

# Installation
1. Download & Install Anaconda(https://www.anaconda.com) & Jupyter Lab (https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html)
2. Install libraries: Execute 'conda activate dev' & 'pip show' in CLI or Terminal to see libraries, and use 'pip install' for the libraries not included
    a. import sys
    b. import fire
    c. import questionary
    d. import pandas as pd 
    e. import hvplot.pandas
    f. import numpy as np 
    g. import os
    h. import json
    i. import requests
    j. from pathlib import Path
    k. from dotenv import load_dotenv
    l. import alpaca_trade_api as api
    m. %matplotlib inline
    n. import altair as alt
3. Clone the Equity-Analysis-Tool Main Branch Repository to your Local Machine
4. Sign up for a free account at https://app.alpaca.markets/login from here you will be able to create your API Keys
5. Configure your personal .env file as below (This file will be hidden)
    ALPACA_API_KEY  = "API Key Goes Here" 
    ALAPACA_API_SECRET_KEY = "API Secret Key Goes Here"
6. Go to your local machine's CLI or Terminal and navigate to the Equity-Analysis-Tool Directory
7. Activate your Conda Development Environment ('conda activate dev') and run the app.py file to start the Equity-Analysis-Tool Client Application

# Equity Analysis Tool Application
1. After the app.py application has been executed, the client will be prompted for their Portfolio Holding's Tickers and Shares
2. Proceed through the application instructions until the application is complete, where then your data will be exported to a .csv file
3. Check the Resources Folder in the Equity-Analysis-Tool to confirm your .csv file has been successfully created

# Equity Analysis Tool Jupyter Lab Notebook
1. After completion of the Equity Analysis Tool Application, you will navigate to the StockAnalysisReport.ipynb under the ClientConfidentials Folder
2. Launch Jupyter Lab (Enter in Windows CLI or Mac Terminal: 'Jupyter Lab' Command) *This will open a web page on your localhost machine with the notebook
3. Step through each of the Jupyter Notebook cells following the instructionto review the your Client Ticker & ETF Risk and Return Analysis Report
