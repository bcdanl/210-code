#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 11:07:55 2025

@author: bchoe
"""



# %%
# =============================================================================
# read_html
# =============================================================================
import pandas as pd

# this causes error
# HTTPError: Too Many Requests
df = pd.read_html('https://finance.yahoo.com/quote/MSFT/history/')




# %%
# =============================================================================
# Using Selenium .get_attribute('outerHTML')
# =============================================================================
import pandas as pd
import os
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from io import StringIO


# Create an instance of Chrome options
options = Options()
options.add_argument("window-size=1400,1200")  # Set the browser window size to 1400x1200
options.add_argument('--disable-blink-features=AutomationControlled')  # Prevent detection of automation by disabling blink features
options.page_load_strategy = 'eager'  # Load only essential content first, skipping non-critical resources

# Initialize the Chrome WebDriver with the specified options
driver = webdriver.Chrome(options=options)  # Correct implementation


# url = 'https://finance.yahoo.com/quote/MSFT/history/'
# driver.get(url)


# %%
# Load content page
url = 'https://finance.yahoo.com/quote/MSFT/history/?p=MSFT&period1=1672531200&period2=1743379200'
driver.get(url)
time.sleep(random.uniform(2, 3))  # wait for table to load

# HTML source
driver.page_source

# Extract the <table> HTML element
table_html = driver.find_element(By.TAG_NAME, 'table').get_attribute('outerHTML')

table_html

# Parse the HTML table into a pandas DataFrame
# df = pd.read_html(StringIO(table_html))[0]

df = pd.read_html(table_html)[0]
df.info()
 # Adj Close Adjusted close price adjusted for splits and dividend and/or capital gain distributions.

# %%
# =============================================================================
# 
# =============================================================================
symbols = ['AAPL', 'MSFT', 'NVDA']


df_all = pd.DataFrame()
for symbol in symbols:
    url = f'https://finance.yahoo.com/quote/{symbol}/history/?p={symbol}&period1=1672531200&period2=1743379200'
    driver.get(url)
    time.sleep(random.uniform(2, 3))  # wait for table to load
    table_html = driver.find_element(By.TAG_NAME, 'table').get_attribute('outerHTML')
    table_html = StringIO(table_html)
    df = pd.read_html(table_html)[0]
    df['Symbol'] = symbol
    df_all = pd.concat([df_all, df], ignore_index=True)
    


# %%
# =============================================================================
# APIs
# =============================================================================

import requests

p = 'https://bcdanl.github.io/210'
response = requests.get(p)  
print(response.status_code)  

p = 'https://bcdanl.github.io/2100'
response = requests.get(p)  
print(response.status_code)  


# %%
# =============================================================================
# BLANK
# =============================================================================



