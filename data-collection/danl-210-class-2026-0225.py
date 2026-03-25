#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 25 10:28:47 2026

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

url = "https://qavbox.github.io/demo/webtable/"
driver.get(url)

driver.find_element(By.XPATH, 
                    '//*[@id="table01"]/tbody/tr[2]/td[3]/a').get_attribute('href')


driver.find_element(By.XPATH, '//*[@id="btn"]').text
driver.find_element(By.XPATH, '//*[@id="btn"]').get_attribute('value')


href = driver.find_element(By.LINK_TEXT, "Selen").get_attribute("href")

driver.find_element(By.LINK_TEXT, "Selenium")


try:
    href = driver.find_element(By.LINK_TEXT, "Selen").get_attribute("href")
except:
    href = ""



random.uniform(0.5, 1.5)
random.uniform(3, 5)

# Example: polite delay between actions/pages
time.sleep(random.uniform(3, 5))  # small jitter (adjust as needed)


driver.get(url)
time.sleep(random.uniform(3, 5))


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


quotes = driver.find_elements(By.CLASS_NAME, 'text')
quotes[0].text
quotes[1].text
quotes[2].text

authors = driver.find_elements(By.CLASS_NAME, 'author')
authors[0].text
authors[1].text
authors[2].text
authors[9].text

tags_all = driver.find_elements(By.CLASS_NAME, 'tags')
tags_all[0].text
# Out[133]: 'Tags: change deep-thoughts thinking world'

tags_all[1].text

abouts = driver.find_elements(By.LINK_TEXT, '(about)')

abouts[0].get_attribute('href')
abouts[1].get_attribute('href')
abouts[2].get_attribute('href')
abouts[4].get_attribute('href')



df = pd.DataFrame()
for p in range(1, 11):
    f_url = f'https://quotes.toscrape.com/page/{p}'
    driver.get(f_url)
    time.sleep( random.uniform(1, 2) )
    
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

























