#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 10:15:47 2026

@author: bchoe
"""

# %%
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
# time.sleep()
# =============================================================================
url = "https://qavbox.github.io/demo/delay/"
driver.get(url)

xpath_click_me = '//*[@id="one"]/input'
driver.find_element(By.XPATH, xpath_click_me).click()

time.sleep(2)  # blind wait: always 2 seconds
              # //*[@id="two"]

xpath_text = '//*[@id="two"]'
element = driver.find_element(By.XPATH, xpath_text)
element.text

element_5sec = driver.find_element(By.XPATH, xpath_text)
element_5sec.text


# //*[@id="two"]


driver.get(url)

xpath_click_me = '//*[@id="one"]/input'
driver.find_element(By.XPATH, xpath_click_me).click()

time.sleep(6)  # blind wait: always 2 seconds
              # //*[@id="two"]

xpath_text = '//*[@id="two"]'
element = driver.find_element(By.XPATH, xpath_text)
element.text


# %%
# =============================================================================
# WebDriverWait() + EC.presence_of_element_located()
# =============================================================================

wait = WebDriverWait(driver, 10)

driver.get(url)
time.sleep(1)
driver.find_element(By.XPATH, xpath_click_me).click()

element2 = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, xpath_text)
        )
)

element2.text




# %%
# =============================================================================
# Classwork 9
# =============================================================================

wait = WebDriverWait(driver, 10)

driver.get(url)
time.sleep(1)

xpath_try_me = '//*[@id="oneMore"]/input[1]'
try_me = driver.find_element(By.XPATH, xpath_try_me)

try_me.click()

# find_element() causes error
# element_delay = driver.find_element(By.ID, 'delay')

element_delay = wait.until(
    EC.presence_of_element_located(
        (By.ID, 'delay')
        )
)

element_delay.text



# %%
# =============================================================================
# This section is blank.
# =============================================================================


