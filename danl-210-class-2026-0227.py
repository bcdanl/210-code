#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 27 10:31:11 2026

@author: bchoe
"""


# %%
# =============================================================================
# Classwork 5
# Part 1
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

url = 'https://quotes.toscrape.com/'
driver.get(url)



# %%
# =============================================================================
# For-loop construction
# =============================================================================
df = pd.DataFrame()
for p in range(1, 11):
    f_url = f'https://quotes.toscrape.com/page/{p}'
    driver.get(f_url)
    time.sleep( random.uniform(1, 2) )   # Be polite: pause between requests to reduce load on the server
    
    quotes = driver.find_elements(By.CLASS_NAME, 'text')
    authors = driver.find_elements(By.CLASS_NAME, 'author')
    tags_all = driver.find_elements(By.CLASS_NAME, 'tags')
    abouts = driver.find_elements(By.LINK_TEXT, '(about)')
    
    for item in range( len(quotes) ):      
        
        quote = quotes[item].text
        author = authors[item].text
        tags = tags_all[item].text
        about = abouts[item].get_attribute('href')
        
        obs_lst = [quote, author, tags, about]
        obs_df = pd.DataFrame([obs_lst])
        
        df = pd.concat([df, obs_df])
        
df.columns =['quote', 'author', 'tags', 'about']
df.to_csv('data/quotes_2026_0225.csv', index = False)



# %%
# =============================================================================
# Part 2. Author DataFrame
# =============================================================================

# Keep only the 'about' column (this column contains each author's profile/about URL)
author_url = df[["about"]]

# Remove duplicate URLs so each author's URL appears only once
author_url = author_url.drop_duplicates()

# Convert the 'about' column (a pandas Series) 
  # into a Python list.
author_url_lst = author_url['about'].tolist()




df_authors = pd.DataFrame()
for item in author_url_lst:
    driver.get(item)
    s = random.uniform(1, 2)
    time.sleep(s)
    
    born_date = driver.find_element(By.CLASS_NAME, 
                                    "author-born-date").text
    
    born_location = driver.find_element(By.CLASS_NAME, 
                                    "author-born-location").text
    
    author_description = driver.find_element(By.CLASS_NAME, 
                                    "author-description").text
    
    obs_lst = [item, born_date, born_location, author_description]
    df_obs = pd.DataFrame([obs_lst])
    df_authors = pd.concat([df_authors, df_obs], ignore_index=True)


df_authors.columns = ['about_url', 'born_date', 
                      'born_location', 'author_description']

df_authors.to_csv('data/quote_authors.csv', index = False)



# %%
# =============================================================================
# Part 1. Question 2
# =============================================================================

# Now suppose you do not know how many pages exist.

# Instead of guessing the last page number, do this:

# Start at page 1
# Scrape the quotes on the current page
# Click the Next button
# Repeat until the Next button is not found

url = 'https://quotes.toscrape.com/'
driver.get(url)

df = pd.DataFrame()

while True:
# for p in range(1, 11):
    # f_url = f'https://quotes.toscrape.com/page/{p}'
    # driver.get(f_url)
    
    try:
        next_btn = driver.find_element(By.PARTIAL_LINK_TEXT,
                                       "Next")
    except:
        next_btn = []
    
    quotes = driver.find_elements(By.CLASS_NAME, 'text')
    authors = driver.find_elements(By.CLASS_NAME, 'author')
    tags_all = driver.find_elements(By.CLASS_NAME, 'tags')
    abouts = driver.find_elements(By.LINK_TEXT, '(about)')
    
    for item in range( len(quotes) ):      
        
        quote = quotes[item].text
        author = authors[item].text
        tags = tags_all[item].text
        about = abouts[item].get_attribute('href')
        
        obs_lst = [quote, author, tags, about]
        obs_df = pd.DataFrame([obs_lst])
        
        df = pd.concat([df, obs_df])
    
    if next_btn != []:
        next_btn.click()
    else:
        break
    
    time.sleep( random.uniform(1, 2) )   # Be polite: pause between requests to reduce load on the server
    
df.columns =['quote', 'author', 'tags', 'about']
df.to_csv('data/quotes_2026_0227.csv', index = False)









