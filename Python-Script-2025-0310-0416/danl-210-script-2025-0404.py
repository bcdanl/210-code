#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 10:36:20 2025

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
# Wait
# =============================================================================

# example webpage
url = "https://qavbox.github.io/demo/delay/"
driver.get(url)
driver.find_element(By.XPATH, '//*[@id="one"]/input').click()
time.sleep(6)
element = driver.find_element(By.XPATH, '//*[@id="two"]') # //*[@id="two"] is xpath
element.text



driver.get(url)
driver.find_element(By.XPATH, '//*[@id="one"]/input').click()
driver.implicitly_wait(10)
element = driver.find_element(By.XPATH, '//*[@id="two"]') # //*[@id="two"] is xpath
element.text


# //*[@id="oneMore"]/input[1]
driver.find_element(By.XPATH, '//*[@id="oneMore"]/input[1]').click()
driver.implicitly_wait(10)  # Wait up to 10 seconds for elements to appear
element2 = driver.find_element(By.ID, 'delay')
element2.text


# %%
# =============================================================================
# Explicit Wait
# =============================================================================
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# CW 10. Question 1


# Use selenium to get to https://qavbox.github.io/demo/delay/.
# Use selenium to click the button with “Click me!”
# Use selenium to locate the text element that will be displayed after 5 seconds using WebDriverWait with EC.presence_of_element_located.
# Its XPath is '//*[@id="two"]'


driver.get(url)
driver.find_element(By.XPATH, '//*[@id="one"]/input').click()
element = ( 
  WebDriverWait(driver, 20)  # 20 is timeout in seconds when an expectation is called
  .until(
    EC.visibility_of_element_located(
      (By.XPATH, '//*[@id="two"]')
      )
    )
)
element.text




# %%
# =============================================================================
# CW10 - Q2
# =============================================================================

url = 'https://www2.census.gov/programs-surveys/popest/tables/2010-2019/counties/totals/'

driver.get(url)
# xpath = '/html/body/table/tbody/tr[4]/td[2]/a'
         # /html/body/table/tbody/tr[5]/td[2]/a

table = driver.find_element(By.XPATH, '/html/body/table/tbody')
rows = table.find_elements(By.TAG_NAME, 'tr')


# /html/body/table/tbody/tr[212]


for i in range(4, len(rows) + 1):
    xpath = f'/html/body/table/tbody/tr[{i}]/td[2]/a'
    driver.find_element(By.XPATH, xpath).click()






# %%
# =============================================================================
# This sectio is left blank intentionally
# =============================================================================
