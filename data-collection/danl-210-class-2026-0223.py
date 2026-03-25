# %%
# =============================================================================
# Classwork 4 - xpath approach
# =============================================================================

# %%
# =============================================================================
# Question 1
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

url = 'https://www.eia.gov/petroleum/gasdiesel/gaspump_hist.php'

driver.get(url)


# find the number of rows
xpath_tbody = '/html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody'
tbody = driver.find_element(By.XPATH, 
                            xpath_tbody)

rows =tbody.find_elements(By.TAG_NAME, 
                          'tr')

nrows = len(rows)

thead = driver.find_element(By.TAG_NAME, 
                            'thead')

cols = thead.find_elements(By.TAG_NAME, 'th')
ncols = len(cols)

# mon-yr xpath
# /html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[1]/td[1]
# /html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[2]/td[1]
# /html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[3]/td[1]

# retail_price
# /html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[1]/td[2]
# /html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[2]/td[2]


# crude-oil
# /html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[1]/td[6]
# /html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[2]/td[6]


# list(range(1, nrows + 1))


# empty DataFrame
df = pd.DataFrame()
for i in range(1, nrows + 1):
    xpath_mon_yr = f'/html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[{i}]/td[1]'
    xpath_rprice = f'/html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[{i}]/td[2]'
    xpath_refining = f'/html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[{i}]/td[3]'
    xpath_dist_mkt = f'/html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[{i}]/td[4]'
    xpath_taxes = f'/html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[{i}]/td[5]'
    xpath_crude_oil = f'/html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[{i}]/td[6]'
    
    mon_yr = driver.find_element(By.XPATH, xpath_mon_yr).text
    retail_price = driver.find_element(By.XPATH, xpath_rprice).text
    refining = driver.find_element(By.XPATH, xpath_refining).text
    dist_mkt = driver.find_element(By.XPATH, xpath_dist_mkt).text
    taxes = driver.find_element(By.XPATH, xpath_taxes).text
    crude_oil = driver.find_element(By.XPATH, xpath_crude_oil).text
    
    obs_list = [mon_yr, retail_price, refining, dist_mkt, taxes, crude_oil]
    obs = pd.DataFrame( [ obs_list ] )
    df = pd.concat([df, obs])
    

df.columns = ['mon_yr', 'retail_price', 'refining', 'dist_mkt', 
              'taxes', 'crude_oil']

df.to_csv('data/eia_2026_0223.csv', index = False)




# %%
# =============================================================================
# Question 2
# =============================================================================

# XPath with nested for-loop
for i in range(1, 10):
    
    for j in range(1, 4):
        xpath = f'//*[@id="main-content"]//table/tbody/tr[{i}]/td[{j}]'
        print(xpath)





# TODO: find out the number of rows (<tr>) and the number of columns (<td>) in each row in the body table (<tbody>)
tbody = driver.find_element(By.TAG_NAME, 'tbody')
rows =tbody.find_elements(By.TAG_NAME, 'tr')
nrows = len(rows)

thead = driver.find_element(By.TAG_NAME, 'thead')
cols = thead.find_elements(By.TAG_NAME, 'th')
ncols = len(cols)

df = pd.DataFrame()
for i in range(1, nrows + 1):
  
    data = []    # creating an empty list for one row
    
    for j in range(1, ncols + 1):  # Iterate over column positions
        
        # TODO: scrape each cell's text in a single row
        xpath_value = f'/html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[{i}]/td[{j}]'
        value = driver.find_element(By.XPATH, xpath_value).text
        
        # TODO: append value to the data list
        data.append(value)
        
    obs = pd.DataFrame([data])
    df = pd.concat([df, obs], ignore_index=True)
    

df.columns = ['mon_yr', 'retail_price', 'refining', 'dist_mkt', 
              'taxes', 'crude_oil']

df.to_csv('data/eia_q2_2026_0223.csv', index = False)
