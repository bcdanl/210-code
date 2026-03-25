#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 23:07:50 2026

@author: bchoe
"""

import pandas as pd
import os, time, random
from io import StringIO

# Import the necessary modules from the Selenium library
from selenium import webdriver  # Main module to control the browser
from selenium.webdriver.common.by import By  # Helps locate elements on the webpage
from selenium.webdriver.chrome.options import Options  # Allows setting browser options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException

# Set the working directory path
wd_path = '/Users/bchoe/Documents/DANL-210' # e.g., '/Users/bchoe/Documents/DANL-210'
os.chdir(wd_path)  # Change the current working directory to wd_path
os.getcwd()  # Retrieve and return the current working directory

# Create an instance of Chrome options
options = Options()

# Initialize the Chrome WebDriver with the specified options
driver = webdriver.Chrome(options=options)


# Load content page
url = 'https://finance.yahoo.com/quote/MSFT/history/?p=MSFT&period1=1672531200&period2=1772323200'
driver.get(url)
time.sleep(random.uniform(4, 8))  # wait for table to load


dfs = pd.read_html(url)


# Extract the <table> HTML element
table_html = driver.find_element(By.TAG_NAME, 'table').get_attribute("outerHTML")

# Parse the HTML table into a pandas DataFrame
dfs = pd.read_html( StringIO(table_html) )

df = dfs[0]

# Filter rows where the 'Open' column contains the word 'Dividend' (these represent dividend entries)
df_dividend = df[df['Open'].str.contains('Dividend', na=False)]

# Filter out dividend rows to keep only stock price data
df_stock = df[~df['Open'].str.contains('Dividend', na=False)]



# %%
# =============================================================================
# Classwork 7
# =============================================================================

lst = ['AAPL', 'MSFT', 'NVDA']

# Example: Yahoo Finance "Historical Data" page (MSFT)
# url = "https://finance.yahoo.com/quote/MSFT/history/?p=MSFT&period1=1672531200&period2=1772323200"

dfs = pd.DataFrame()
for company in lst:
    
    url = f"https://finance.yahoo.com/quote/{company}/history/?p={company}&period1=1672531200&period2=1772323200"
    driver.get(url)
    time.sleep(random.uniform(4, 8))
    
    
    # Extract the <table> HTML element
    table_html = driver.find_element(By.TAG_NAME, 'table').get_attribute("outerHTML")
    
    # Parse the HTML table into a pandas DataFrame
    df = pd.read_html( StringIO(table_html) )[0]
    
    df['company'] = company
    
    dfs = pd.concat([dfs, df], ignore_index=True)
    



# %%
# =============================================================================
# 
# =============================================================================


import requests

p = 'https://bcdanl.github.io/210'
response = requests.get(p)
print(response.status_code)
print(response.reason)


p = 'https://bcdanl.github.io/2100'
response = requests.get(p)
print(response.status_code)
print(response.reason)


# %%
# =============================================================================
# 
# =============================================================================


