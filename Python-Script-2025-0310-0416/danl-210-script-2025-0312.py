#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 10:30:01 2025

@author: bchoe
"""


# %%
# =============================================================================
# read_html()
# =============================================================================
import pandas as pd
url = "https://www.nps.gov/orgs/1207/national-park-visitation-sets-new-record-as-economic-engines.htm"

tables = pd.read_html(url)
len(tables)

df_0 = tables[0]
df_1 = tables[1]


df_0.columns
df_0.iloc[0]

df_0.columns = df_0.iloc[0]
df_0.columns
df_0 = df_0[1:]
df_0 = df_0.reset_index()



df_0 = tables[0]
df_0.columns = df_0.iloc[0]  # Set the first row as column names
df_0 = df_0[1:].reset_index(drop=True)  # Remove the first row & reset index

# %%
# =============================================================================
# to_csv()
# =============================================================================
# Import the os module to interact with the operating system
import os  

# Set the working directory path
wd_path = '/Users/bchoe/My Drive/suny-geneseo/spring2025/lecture-code/data-210' # Do not choose your personal website folder
os.chdir(wd_path)  # Change the current working directory to wd_path
os.getcwd()  # Retrieve and return the current working directory

# index=False to not write the row index in the CSV output
df_0.to_csv('table.csv')
df_0.to_csv('table_no_index.csv', index = False)






# %%
# =============================================================================
# CW 8. Q1
# =============================================================================
# pd.to_datetime() with format='%b-%y'.

url = "https://www.eia.gov/petroleum/gasdiesel/gaspump_hist.php"
df = pd.read_html(url)
df_0 = df[0]

df_0['Mon-yr'] = pd.to_datetime(df_0['Mon-yr'], format='%b-%y')
df_0['Mon-yr'] = df_0['Mon-yr'].str.replace('July', 'Jul')

df_0['Mon-yr'] = pd.to_datetime(df_0['Mon-yr'], format='%b-%y')
df_0['Mon-yr'] = df_0['Mon-yr'].str.replace('Sept', 'Sep')

df_0['Mon-yr'] = pd.to_datetime(df_0['Mon-yr'], format='%b-%y')

df_0.to_csv('eia_2025_03.csv', index = False)


# %%
# =============================================================================
# CW 8. Q2
# =============================================================================

url = 'https://www.geneseo.edu/business/student%20outcomes'
dfs = pd.read_html(url)

df_0 = dfs[0]
df_1 = dfs[1]
df_2 = dfs[2]
df_3 = dfs[3]
df_4 = dfs[4]

df_0.columns
df_1.columns

df_1.columns = df_1.iloc[1]
df_1 = df_1[2:].reset_index(drop=True)

df_1.to_csv('sob_graduation_rate.csv', index = False)


# %%
# =============================================================================
# requests
# =============================================================================
import requests

p = 'https://bcdanl.github.io/210'
response = requests.get(p)  
print(response.status_code)  
print(response.reason)      


p = 'https://bcdanl.github.io/2100'
response = requests.get(p)  
print(response.status_code)  
print(response.reason)      



