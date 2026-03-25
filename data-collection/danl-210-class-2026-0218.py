#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 10:32:47 2026

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


form_url = "https://qavbox.github.io/demo/webtable/"
driver.get(form_url)

# driver.close()
# driver.quit()

form = driver.find_element(By.ID, "form1")
form.text


home_btn = driver.find_element(By.CLASS_NAME, "btn")
home_btn.click()

driver.back()

home_btn2 = driver.find_element(By.NAME, "home")
home_btn2.click()

driver.back()

home_btn3 = driver.find_element(By.CSS_SELECTOR, 
                                "body > div > a > input")

home_btn3.click()
driver.back()


table01 = driver.find_element(By.ID, "table01")

table01_colname = table01.find_element(By.TAG_NAME, "thead")
table01_colname.text


selenium_link = driver.find_element(By.LINK_TEXT, "Selenium")
selenium_link.click()

driver.back()

qavlinks = driver.find_element(By.PARTIAL_LINK_TEXT, "qav")
qavlinks.click()
driver.back()

qavlinks_list = driver.find_elements(By.PARTIAL_LINK_TEXT, "qav")
qavlinks_list[0]

qavlinks_list[0].click()
qavlinks_list[1].click()


driver.back()

# XPath for Selenium link in the first table
# //*[@id="table01"]/tbody/tr[2]/td[3]/a

# Full XPath for Selenium link in the first table
# /html/body/form/fieldset/div/table/tbody/tr[2]/td[3]/a



table02 = driver.find_element(By.XPATH,
                              '//*[@id="table02"]')

table02.find_element(By.TAG_NAME, "thead").text


t01 = driver.find_element(By.TAG_NAME, "table")
t01.find_element(By.TAG_NAME, "thead").text



