#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 14 10:57:14 2025

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
# Classwork 9
# =============================================================================

driver.get('https://www.eia.gov/petroleum/gasdiesel/gaspump_hist.php')


xpath_tab = '/html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody'
table = driver.find_element(By.XPATH, xpath_tab)
nrow = table.find_elements(By.TAG_NAME, 'tr')




# /html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[2]/td[1]
# /html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[3]/td[1]
# /html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[302]/td[1]

# /html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[1]/td[2]
# /html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[1]/td[6]


df = pd.DataFrame()
for item in range(1, len(nrow) + 1):
    
    xpath_monyr = f'/html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[{item}]/td[1]'
    xpath_retailP = f'/html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[{item}]/td[2]'
    xpath_refining = f'/html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[{item}]/td[3]'
    xpath_distMkt = f'/html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[{item}]/td[4]'
    xpath_tax = f'/html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[{item}]/td[5]'
    xpath_crudeOil = f'/html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[{item}]/td[6]'
    
    v_monyr = driver.find_element(By.XPATH, xpath_monyr).text
    v_retailP = driver.find_element(By.XPATH, xpath_retailP).text
    v_refining = driver.find_element(By.XPATH, xpath_refining).text
    v_distMkt = driver.find_element(By.XPATH, xpath_distMkt).text
    v_tax = driver.find_element(By.XPATH, xpath_tax).text
    v_crudeOil = driver.find_element(By.XPATH, xpath_crudeOil).text
    
    lst = [ v_monyr, v_retailP, v_refining, v_distMkt, v_tax, v_crudeOil ]
    obs = pd.DataFrame( [ lst ] )
    df = pd.concat([df, obs])

df.columns = ['mon_yr', 'retail_price', 'refining', 'dist_mkt', 'taxes', 'crude_oil']
df = df.reset_index(drop = True)

df.to_csv('data/webscrapping_eia_2025_0327.csv', index = False)



# %%
# double for-loop

thead = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/thead')
ncol = thead.find_elements(By.TAG_NAME, 'th')

df2 = pd.DataFrame()
for item in range(1, len(nrow) + 1):
    
    lst = []
    for col in range(1, len(ncol) + 1):
        xpath = f'/html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[{item}]/td[{col}]'
        v = driver.find_element(By.XPATH, xpath).text
        lst.append(v)
        obs = pd.DataFrame( [ lst ] )

    df2 = pd.concat([df2, obs])


# %%
# Classwork 9, Question 2


url = 'https://quotes.toscrape.com/'
driver.get(url)

while True:
    next_btn = driver.find_element(By.CLASS_NAME, 'next')
    
    # if next btn exists, click it. otherwise, break the loop
    if next_btn != [] :
        next_btn.click()
    else:
        break
    



