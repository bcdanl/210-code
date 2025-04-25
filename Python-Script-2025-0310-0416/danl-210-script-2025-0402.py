#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 10:31:52 2025

@author: bchoe
"""

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
# Classwork 9 - Question 2
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
    s = random.uniform(2, 3)
    time.sleep(s)
    
df.columns = ['quote', 'author', 'tag', 'about']
# %%
# =============================================================================
# About
# =============================================================================
    
about = df['about'].drop_duplicates()
about = about.tolist()

# driver.get(about[0])

df_author = pd.DataFrame()
for i in range(len(about)):
    driver.get(about[i])
    about_url = about[i]
    author_name = driver.find_element(By.CLASS_NAME, 'author-title').text
    author_born_date = driver.find_element(By.CLASS_NAME, 'author-born-date').text
    author_born_location = driver.find_element(By.CLASS_NAME, 'author-born-location').text
    author_desc = driver.find_element(By.CLASS_NAME, 'author-description').text
    obs = [about_url, author_name, author_born_date, author_born_location, author_desc]
    obs = pd.DataFrame([ obs ])
    df_author = pd.concat([df_author, obs])
    s = random.uniform(1,2)
    time.sleep(s)
    
df_author.columns = ['about', 'author_name', 'author_born_date', 'author_born_location', 'author_desc']



# %%
# =============================================================================
# Classwork 9 - Question 2 - tag
# =============================================================================


url = 'https://quotes.toscrape.com/'
driver.get(url)


df_tag = pd.DataFrame()
while True:
    
    try:
        next_btn = driver.find_element(By.PARTIAL_LINK_TEXT, 'Next')
    except:
        next_btn = []
        
    tagss = driver.find_elements(By.CLASS_NAME, 'tag')

    
    for item in range( len(tagss)  ):
        tag = tagss[item].text
        obs = [tag]
        obs = pd.DataFrame( [obs] )
        df_tag = pd.concat([df_tag, obs], ignore_index=True)
    
    # if next btn exists, click it. otherwise, break the loop
    if next_btn != [] :
        next_btn.click()
    else:
        break
    
    # time.sleep(3)
    # s = random.uniform(2, 3)
    # time.sleep(s)

df_tag.columns = ['tag']

df_tag_sorted = (
    df_tag['tag']
    .value_counts()
    .reset_index()
    .nlargest(15, 'count', keep = 'all')
    ) 


df.to_csv('data/df_quotes.csv', index = False,
          encoding='utf-8-sig')


df_author.to_csv('data/df_authors.csv', index = False,
          encoding='utf-8-sig')



# %%
# =============================================================================
# Wait
# =============================================================================

# example webpage
url = "https://qavbox.github.io/demo/delay/"
driver.get(url)

driver.find_element(By.XPATH, '//*[@id="one"]/input').click()
# time.sleep(5)
element = driver.find_element(By.XPATH, '//*[@id="two"]')
element.text



# %%
# =============================================================================
# This section is left blank intentionally
# =============================================================================
