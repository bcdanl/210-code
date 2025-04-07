#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 10:34:56 2025

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
# CW10 - Q2
# =============================================================================

url = 'https://www2.census.gov/programs-surveys/popest/tables/2010-2019/counties/totals/'

driver.get(url)
# xpath = '/html/body/table/tbody/tr[4]/td[2]/a'
         # /html/body/table/tbody/tr[5]/td[2]/a
         # /html/body/table/tbody/tr[211]/td[2]/a
table = driver.find_element(By.XPATH, '/html/body/table/tbody')
rows = table.find_elements(By.TAG_NAME, 'tr')


# /html/body/table/tbody/tr[212]


for i in range(4, len(rows) + 1):
    xpath = f'/html/body/table/tbody/tr[{i}]/td[2]/a'
    driver.find_element(By.XPATH, xpath).click()
    # time.sleep(random.uniform(0, .5))

# ElementClickInterceptedException: 
    # element click intercepted: 
        # Element <a href="...">co-est2019-comp-53.xlsx</a> 
        # is not clickable at point (108, 9). 
        # Other element would receive the click: 
            # <a href="...">co-est2019-cumchg-34.xlsx</a>


# %%
# =============================================================================
# CW10 - Q3
# =============================================================================

url = 'http://books.toscrape.com'
driver.get(url)
time.sleep(1)

cat_lst = driver.find_element(By.XPATH, '/html/body/div/div/div/aside/div[2]/ul/li/ul')
cats = cat_lst.find_elements(By.TAG_NAME, 'li')

# cat = driver.find_element(By.XPATH, '/html/body/div/div/div/aside/div[2]/ul/li/ul/li[1]/a')
# cat.click()
# cat.text
# driver.back()

df = pd.DataFrame()
for i in range(1, len(cats) + 1):
    xpath_cat = f'/html/body/div/div/div/aside/div[2]/ul/li/ul/li[{i}]/a'
    cat = driver.find_element(By.XPATH, xpath_cat)
    category = cat.text
    cat.click()
    
    while True:
        
        try:
            btn = driver.find_element(By.LINK_TEXT, 'next')
        except:
            btn = []
        
        xpath_bookList = '/html/body/div/div/div/div/section/div[2]/ol'
        bookList = driver.find_element(By.XPATH, xpath_bookList)
        books = bookList.find_elements(By.TAG_NAME, 'h3')
        prices = bookList.find_elements(By.CLASS_NAME, 'price_color')
        prices[0].text
        # books[0].find_element(By.TAG_NAME, 'a').get_attribute('title')
        # books[1].find_element(By.TAG_NAME, 'a').get_attribute('title')
        
        
        for j in range(len(books)):
            title = books[j].find_element(By.TAG_NAME, 'a').get_attribute('title')
            price = prices[j].text
            lst = [category, title, price]
            obs = pd.DataFrame([ lst ])
            df = pd.concat([df, obs], ignore_index=True)
            
        if btn != []:
            btn.click()
        else:
            break
            
        
df.columns = ['category', 'title', 'price']


# %%
# =============================================================================
# pandas
# =============================================================================


# Find the most expensive book 
df['price'] = df['price'].str.replace('£', '')
df['price'] = df['price'].astype('float')
df['price']

top1 = df.nlargest(1, 'price', keep='all')
top1        

# Find the category with the most number of books.
n_books = (
    df['category']
    .value_counts()
    .reset_index()
    .nlargest(1, 'count', keep = 'all')
    )
n_books

# %%
# =============================================================================
# This sectio is left blank intentionally
# =============================================================================
