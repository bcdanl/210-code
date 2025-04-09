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

df = pd.read_html('https://finance.yahoo.com/quote/MSFT/history/')






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

# Initialize the Chrome WebDriver with the specified options
driver = webdriver.Chrome(options=options)  # Correct implementation


# url = 'https://finance.yahoo.com/quote/MSFT/history/'
# driver.get(url)

# Load content page
url = 'https://finance.yahoo.com/quote/MSFT/history/?p=MSFT&period1=1672531200&period2=1743379200'
driver.get(url)
time.sleep(random.uniform(3, 5))  # wait for table to load


# Extract the <table> HTML element
table_html = driver.find_element(By.TAG_NAME, 'table').get_attribute('outerHTML')

# Parse the HTML table into a pandas DataFrame
df = pd.read_html(table_html)[0]
df[0]


# %%

symbols = ['AAPL', 'MSFT', 'NVDA']


df_all = pd.DataFrame()
for symbol in symbols:
    url = f'https://finance.yahoo.com/quote/{symbol}/history/?p={symbol}&period1=1672531200&period2=1743379200'
    driver.get(url)
    time.sleep(random.uniform(3, 5))  # wait for table to load
    table_html = driver.find_element(By.TAG_NAME, 'table').get_attribute('outerHTML')
    df = pd.read_html(table_html)[0]
    df_all = pd.concat([df_all, df], ignore_index=True)
    







