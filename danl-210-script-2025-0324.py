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




home_button3 = driver.find_element(By.CSS_SELECTOR, 'body > div > a > input')
home_button3.click()
driver.back()



table_01 = driver.find_element(By.ID, 'table01')
table_01.text


table_01.find_element(By.TAG_NAME, 'thead').text


selenium_link = driver.find_element(By.LINK_TEXT, 'Selenium')
selenium_link.click()


Selen_link = driver.find_element(By.PARTIAL_LINK_TEXT, 'qav')
Selen_link.click()
driver.back()


Selen_links = driver.find_elements(By.PARTIAL_LINK_TEXT, 'qav')


# find_elements

Selen_links[1].click()
Selen_links[0].click()



# %%
# =============================================================================
# 
# =============================================================================


xpath = '//*[@id="table02"]/thead/tr/th[1]'
xpath_abs = '/html/body/form/fieldset/div/div/table/thead/tr/th[1]'



table_tags = driver.find_elements(By.TAG_NAME, 'tr')

table_tags[0].text

table_tags[60].text
table_tags[59].text


btn = driver.find_element(By.ID, 'btn')

btn.text

ex = driver.find_element(By.XPATH, '/html/body/form/fieldset/div/table/tbody/tr[2]/td[3]/a')

ex.text
ex.click()
driver.back()

ex.get_attribute('href')



driver.find_element(By.XPATH, '//*[@id="btn"]').get_attribute('value')



# %%
# =============================================================================
# Classwork 9
# =============================================================================


driver.get('https://www.eia.gov/petroleum/gasdiesel/gaspump_hist.php')



for i in range(1, 10):
    xpath = f'/html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[{i}]/td[1]'
    print(xpath)




