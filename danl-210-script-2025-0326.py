#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 14 10:57:14 2025

@author: bchoe
"""

#%%
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



# %%
# =============================================================================
# Classwork 9
# =============================================================================


driver.get('https://www.eia.gov/petroleum/gasdiesel/gaspump_hist.php')




# /html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[1]/td[2]
# /html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[2]/td[1]
# /html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[2]/td[2]


# table body
# 

xpath_tab = '/html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody'
table = driver.find_element(By.XPATH, xpath_tab)

nrow = table.find_elements(By.TAG_NAME, 'tr')
len(nrow)


# lst1 = ['a1', 'b1', 'c1', 'd1', 'e1']
# data1 = pd.DataFrame([ lst1 ])

# lst2 = ['a2', 'b2', 'c2', 'd2', 'e2']
# data2 = pd.DataFrame([ lst2 ])

# df = pd.concat([data1, data2], ignore_index=True)


# below is incomplete yet

df = pd.DataFrame()
for item in range(1, len(nrow)):
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




