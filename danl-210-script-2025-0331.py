#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 10:28:23 2025

@author: bchoe
"""

# %%
# =============================================================================
# Setting up Selenium
# =============================================================================
# Import the necessary modules from the Selenium package
import pandas as pd
import os
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Create an instance of Chrome options
options = Options()
options.add_argument("window-size=1400,1200")  # Set the browser window size to 1400x1200

# Initialize the Chrome WebDriver with the specified options
driver = webdriver.Chrome(options=options)  # Correct implementation

# Now you can use 'driver' to control the Chrome browser

# Set the working directory path
wd_path = '/Users/bchoe/My Drive/suny-geneseo/spring2025/lecture-code' # Do not choose your personal website folder
os.chdir(wd_path)  # Change the current working directory to wd_path
os.getcwd()  # Retrieve and return the current working directory


# %%
# =============================================================================
# Classwork 9 Question 2
# =============================================================================


url = 'https://quotes.toscrape.com/'
driver.get(url)

df = pd.DataFrame()
while True:
    
    try:
        next_btn = driver.find_element(By.PARTIAL_LINK_TEXT, 'Next')
    except:
        next_btn = []
        
    quotes = driver.find_elements(By.CLASS_NAME, 'quote')
    authors = driver.find_elements(By.CLASS_NAME, 'author')
    tags = driver.find_elements(By.CLASS_NAME, 'tags')
    abouts = driver.find_elements(By.PARTIAL_LINK_TEXT, '(about)')

    
    for item in range( len(quotes)  ):
        quote = quotes[item].text
        author = authors[item].text
        tag = tags[item].text
        about = abouts[item].get_attribute('href')
        obs = [quote, author, tag, about]
        obs = pd.DataFrame( [obs] )
        df = pd.concat([df, obs], ignore_index=True)
    
    # if next btn exists, click it. otherwise, break the loop
    if next_btn != [] :
        next_btn.click()
    else:
        break
    
    # time.sleep(3)
    # s = random.uniform(1, 2)
    # time.sleep(s)
    
    
    
    
