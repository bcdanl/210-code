#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 10:31:56 2026

@author: bchoe
"""

# Import the os module to interact with the operating system
import os  
import pandas as pd

url = "https://www.nps.gov/orgs/1207/national-park-visitation-sets-new-record-as-economic-engines.htm"
tables = pd.read_html(url)
len(tables)
df_0 = tables[0]


df_1 = tables[1]
df_1.columns
df_1.columns = df_1.iloc[0]


df_1.columns
df_1 = df_1.iloc[1:]



# Set the working directory path
wd_path = '/Users/bchoe/Documents/DANL-210' # e.g., '/Users/bchoe/Documents/DANL-210'
os.chdir(wd_path)  # Change the current working directory to wd_path
os.getcwd()  # Retrieve and return the current working directory

# index=False to not write the row index in the CSV output
df_0.to_csv('data/table.csv', index =False)
df_0.to_csv('data/table_0.csv')


# %%
# =============================================================================
# pd.read_csv()
# =============================================================================
path_relative = "data/custdata_rev.csv"

# Read the CSV file into a pandas DataFrame.
# pd.read_csv(...) loads the file and creates a table-like object (a DataFrame) in Python.
# After this line runs, df_rel will contain all rows and columns from the CSV.
df_rel = pd.read_csv(path_relative)

path_absolute = "/Users/bchoe/Documents/DANL-210/data/custdata_rev.csv"
df_abs = pd.read_csv(path_absolute)



# %%
# =============================================================================
# Scrapping a web-table
# =============================================================================


url_eia = 'https://www.eia.gov/petroleum/gasdiesel/gaspump_hist.php'
df_eia = pd.read_html(url_eia)
df_eia = df_eia[0]

df_eia.to_csv('data/eia_table.csv', index=False)

df_eia.to_csv('eia_table_new.csv', 
              index=False)

df_eia.to_csv('/Users/bchoe/Documents/DANL-210/eia_table_abs.csv', 
              index=False)




# %%
# =============================================================================
# Scrapping multiple web-tables
# =============================================================================

url_sob = 'https://www.geneseo.edu/business/student-outcomes/'

df_list = pd.read_html(url_sob)

df_sob_0 = df_list[0]
df_sob_1 = df_list[1]
df_sob_2 = df_list[2]
df_sob_3 = df_list[3]
df_sob_4 = df_list[4]


df_sob_1.columns = df_sob_1.iloc[0] + df_sob_1.iloc[1]
df_sob_1 = df_sob_1.iloc[2:]
df_sob_1.columns = ['Program', 'Percent (%)2015-16',
                   'Percent (%)2016-17', 'Percent (%)2017-18',
                   'Percent (%)2018-19', 'Percent (%)2019-20',
                   'Percent (%)5-Year % Change']







# %%
# =============================================================================
# Blank
# =============================================================================





