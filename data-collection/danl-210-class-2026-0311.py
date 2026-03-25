#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 10:29:40 2026

@author: bchoe
"""

import pandas as pd
import requests

headers = {
    'x-pulse-application-version': 'v1.40.15',
    'sec-ch-ua-platform': '"macOS"',
    'Referer': 'https://www.premierleague.com/',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
    'x-pulse-application-name': 'web',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"',
    'sec-ch-ua-mobile': '?0',
}

params = {
    '_sort': 'goal_assists:desc',  # goal_assists:desc   goals:desc
    'country': '',
    '_limit': '50',
}

response = requests.get(
    'https://sdp-prem-prod.premier-league-prod.pulselive.com/api/v3/competitions/8/seasons/2025/players/stats/leaderboard',
    params=params,
    headers=headers,
)

response.status_code

content = response.json()
content.keys()

content_data = content['data']

# to normalized a list of dicts into DataFrame
df_assists = pd.json_normalize(content_data)

df.columns


# %%
# =============================================================================
# Homework 3 - Q1
# =============================================================================
# %%
# =============================================================================
# Part 1
# =============================================================================
import pandas as pd
import numpy as np
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


url = 'https://www.nyc.gov/site/finance/property/property-annualized-sales-update.page'
driver.get(url)


lst_links_dwn = driver.find_elements(By.PARTIAL_LINK_TEXT, "Download")
lst_links_M = driver.find_elements(By.PARTIAL_LINK_TEXT, "M")

lst_links = lst_links_dwn + lst_links_M


lst_links[0].get_attribute('href')

for item in range(len(lst_links)):
    if ".x" in lst_links[item].get_attribute('href'):
        lst_links[item].click()
        time.sleep(random.uniform(1, 1.5))
    



# Locate the element whose link text contains "rolling sales"
bottom_of_page = driver.find_element(
    By.PARTIAL_LINK_TEXT,
    "rolling sales"
)


bottom_of_page.click()
driver.back()

# Scroll until that element is visible in the browser window
driver.execute_script(
    "arguments[0].scrollIntoView();",
    bottom_of_page
)

# Then scroll all the way back to the top of the page
driver.execute_script("window.scrollTo(0, 0);")



# %%
# =============================================================================
# HW3 Part 2
# =============================================================================


import os
import requests
import pandas as pd

# Set the working directory path
wd_path = 'ABSOLUTE_PATHNAME_OF_YOUR_WORKING_DIRECTORY' # e.g., '/Users/bchoe/Documents/DANL-210'
os.chdir(wd_path)  # Change the current working directory to wd_path

url = 'https://bcdanl.github.io/data/fred_api_series_housing_price.csv'
series_housing_price = pd.read_csv(url)
series_id_housing_price = series_housing_price['id'].tolist()


api_key = '80657885ed24a6137d5f63590c0e5c4a'
url = "https://api.stlouisfed.org/"
endpoint = "series/observations"
api_endpoint = url + "fred/" + endpoint

# =============================================================================
# In the above, assign api_key to your FRED API key.
# FILLING IN THE BLANKs (????????) IN THE CODE BELOW 
# =============================================================================

df_all = pd.DataFrame()

for val in series_id_housing_price:    
    param_dict = {
      'api_key': api_key,
      'file_type': 'json',
      'series_id': val
    }
    
    response = requests.get(api_endpoint,
                            params = param_dict)
    
    # time.sleep(....)
    # Convert JSON response to Python dictionary.
    fred = response.json()
    
    # Extract the "observations" list element.
    df = pd.DataFrame( fred['observations'] )

    # To select only 'date' and 'value' columns in the `df` DataFrame
    df = df[['date', 'value']]   
    
    # To add an 'id' column to the `df` DataFrame
    df['id'] = val  
    
    # To append the `df` DataFrame to the `df_all` DataFrame
        # Ensure that a row index of df_all starts from 0, 1, 2, ...
    df_all = pd.concat([df_all, df], ignore_index=True)
    
    

# =============================================================================
# Below transforms the `df_all` DataFrame you have collected.
# Do the following:
# 1. In the last line below, replace "PATHNAME_OF_df_clean.csv" 
#    with your pathname for the CSV file of the `df_clean` DataFrame.
# 2. Then run the code below.
# =============================================================================

# Join
df_clean = df_all.merge(series_housing_price, on = 'id', how = 'left')


# String operations
df_clean['title'] = df_clean['title'].str.replace('Home Price Index (', '')
df_clean[['tier', 'city']] = df_clean['title'].str.split(' Tier\) for ', expand=True)
df_clean[['city', 'state']] = df_clean['city'].str.split(', ', expand=True)

# Selecting variables
df_clean = df_clean[['city', 'state', 'tier', 'date', 'value']]

# Renaming
df_clean = df_clean.rename( columns = { "value": "home_price_index" } )

# Converting Data Types
df_clean = df_clean.astype({'home_price_index': 'float',
                          'date': 'datetime64[ns]'})
tier_order = ['Low', 'Middle', 'High']  # your desired order
df_clean['tier'] = pd.Categorical(df_clean['tier'], categories=tier_order, ordered=True)

# Sorting
df_clean = df_clean.sort_values(['state', 'city', 'date', 'tier'],
                            ascending = [True, True, False, True])
# Exporting DataFrame as a CSV file
df_clean.to_csv("data/fred_2026.csv", index=False)
# =============================================================================
# PROVIDE YOUR CODE FROM HERE
# =============================================================================






