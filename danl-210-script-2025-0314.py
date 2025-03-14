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
from selenium import webdriver  # Main module to control the browser
from selenium.webdriver.common.by import By  # Helps locate elements on the webpage
from selenium.webdriver.chrome.options import Options  # Allows setting browser options

# Create an instance of Chrome options
options = Options()
options.add_argument("window-size=1400,1200")  # Set the browser window size to 1400x1200

# Initialize the Chrome WebDriver with the specified options
driver = webdriver.Chrome(options=options)  # Correct implementation

# Now you can use 'driver' to control the Chrome browser



# %% 
# =============================================================================
# get()
# =============================================================================

form_url = "https://qavbox.github.io/demo/webtable/"
driver.get(form_url)
driver.close()
driver.quit()



# %%
# =============================================================================
# find_element()
# =============================================================================

form1 = driver.find_element(By.ID, "form1")
form1

form1.text



homebtn1 = driver.find_element(By.CLASS_NAME, "homebtn")

homebtn1.click()
driver.back()


home_button2 = driver.find_element(By.NAME, "home")
home_button2.click()
driver.back()














# %%
# =============================================================================
# 
# =============================================================================














