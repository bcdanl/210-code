#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 10:30:59 2026

@author: bchoe
"""

# =============================================================================
# Setup
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


# %%
# =============================================================================
# 
# =============================================================================

driver.get('https://books.toscrape.com')
time.sleep(random.uniform(1, 2))

xpath_category_side = '/html/body/div/div/div/aside/div[2]/ul/li/ul'
category_side = driver.find_element(By.XPATH, xpath_category_side)
categories = category_side.find_elements(By.TAG_NAME, 'li')
n_categories = len(categories)

# categories[0].find_elements(By.TAG_NAME, 'a')

# xpath_cat = '/html/body/div/div/div/aside/div[2]/ul/li/ul/li[1]/a'
# cat = driver.find_element(By.XPATH, xpath_cat)
# cat.click()

df = pd.DataFrame()
for i in range(1, n_categories + 1):
    
    xpath_cat = f'/html/body/div/div/div/aside/div[2]/ul/li/ul/li[{i}]/a'
    cat = driver.find_element(By.XPATH, xpath_cat)
    cat.click()
    
    j = i - 1

    # To deal with 
        # StaleElementReferenceException
    xpath_category_side = '/html/body/div/div/div/aside/div[2]/ul/li/ul'
    category_side = driver.find_element(By.XPATH, xpath_category_side)
    categories = category_side.find_elements(By.TAG_NAME, 'li')
    category = categories[j].text
    
    while True:
        
        try:
            next_btn = driver.find_element(By.PARTIAL_LINK_TEXT, "next")
        except:
            next_btn = []
        
        books = driver.find_elements(By.TAG_NAME, 'h3')
        prices = driver.find_elements(By.CLASS_NAME, 'price_color')
                
        for item in range(len(books)):
            title = books[item].find_element(By.TAG_NAME, 'a').get_attribute("title")
            price = prices[item].text
            
            lst = [category, title, price]
            obs = pd.DataFrame([lst])
            df = pd.concat([df, obs], ignore_index=True)
            
        if next_btn != []:
            next_btn.click()
            time.sleep(random.uniform(1, 2))
        else:
            break
        
            
df.columns = ['category', 'title', 'price']
df.to_csv('data/books.csv', index=False)


# %%
# =============================================================================
# This Sectio is left intentionally as blank.
# =============================================================================
