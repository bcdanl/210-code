#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 20 09:26:01 2026

@author: bchoe
"""

import pandas as pd

df = pd.DataFrame()

names = ["Ava", "Ben", "Chris"]
schools = ["Geneseo", "Buffalo", "Syracuse"]

for i in range(0, 3):
    
    name = names[i]
    school = schools[i]
    
    obs_lst = [i, name, school, 2025]
    
    obs = pd.DataFrame([obs_lst])
    df = pd.concat([df, obs], ignore_index = True)
    
df.columns = ['id', 'name', 'school', 'year']



for i in range(1, 10):
    xpath = f'//*[@id="main-content"]//table/tbody/tr[{i}]/td[1]'
    print(xpath)
    
# %%
# =============================================================================
# Classwork 4
# =============================================================================

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

url = 'https://www.eia.gov/petroleum/gasdiesel/gaspump_hist.php'

driver.get(url)

# TODO: find out the number of rows (<tr>) in the body table (<tbody>)

table = driver.find_element(By.TAG_NAME, 'tbody')
rows = table.find_elements(By.TAG_NAME, 'tr')
nrows = len(rows)

# Mon-yr
# Row 1 
# /html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[1]/td[1]
# Row 2
# /html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[2]/td[1]

# retail price
# /html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[1]/td[2]
# /html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[2]/td[2]

df = pd.DataFrame()
for i in range(1, nrows + 1):

    # TODO: scrape each cell's text in a single row
    
    xpath_mon_yr = f'/html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[{i}]/td[1]'
    xpath_retail_price = f'/html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[{i}]/td[2]'
    xpath_refining = f'/html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[{i}]/td[3]'
    xpath_distribution_marketing = f'/html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[{i}]/td[4]'
    xpath_taxes = f'/html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[{i}]/td[5]'
    xpath_crude_oil = f'/html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[{i}]/td[6]'
    
    mon_yr = driver.find_element(By.XPATH, 
                                 xpath_mon_yr).text
    
    retail_price = driver.find_element(By.XPATH, 
                                       xpath_retail_price).text
    
    refining = driver.find_element(By.XPATH, 
                                   xpath_refining).text
    
    distribution_marketing = driver.find_element(By.XPATH, 
                                                 xpath_distribution_marketing).text
    
    taxes = driver.find_element(By.XPATH, 
                                xpath_refining).text
    
    crude_oil = driver.find_element(By.XPATH, 
                                    xpath_refining).text
    
    
    
    obs_lst = [mon_yr, retail_price, refining, 
               distribution_marketing, taxes, crude_oil]
    obs = pd.DataFrame([obs_lst])
    
    df = pd.concat([df, obs], ignore_index = True)

df.columns = ['mon_yr', 'retail_price', 'refining', 
              'distribution_marketing', 'taxes', 'crude_oil']


df.to_csv('data/eia_2026_0220', index= False)


# %%


