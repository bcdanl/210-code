#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 10:43:44 2025

@author: bchoe
"""

# %%
# =============================================================================
# Libraries
# =============================================================================
import requests
import pandas as pd


# %%
# =============================================================================
# NYC Open Data
# =============================================================================

endpoint = 'https://data.cityofnewyork.us/resource/k397-673e.json'
response = requests.get(endpoint)
content = response.json()

df = pd.DataFrame(content)

# %%
# =============================================================================
# FRED API
# =============================================================================

param_dicts = {
  'api_key': 'YOUR_FRED_API_KEY', ## Change to your own key
  'file_type': 'json',
  'series_id': 'GDPC1'    ## ID for US real GDP
}
url = "https://api.stlouisfed.org/"
endpoint = "series/observations"
api_endpoint = url + "fred/" + endpoint   # sum of strings
response = requests.get(api_endpoint, params = param_dicts)

response.status_code
content = response.json()
content = content['observations'] # to access value of 'observations' in a content dictionary

df = pd.DataFrame(content)
df.info()



# %%
# =============================================================================
# Classwork 11 - Q1
# =============================================================================

url = 'https://data.cityofnewyork.us/resource/c3uy-2p5r.json'
# query parameters (e.g., limit rows)
param_dict = {
    "$limit": 100   # You can increase this to get more observations
}

response = requests.get(url, params= param_dict)
content = response.json()

df_nyc_air = pd.DataFrame(content)



# %%
# =============================================================================
# Classwork 11 - Q2
# =============================================================================

# Real GDP
param_dicts = {
  'api_key': 'YOUR_FRED_API_KEY', ## Change to your own key
  'file_type': 'json',
  'series_id': 'GDPC1'    ## ID for US real GDP
}
url = "https://api.stlouisfed.org/"
endpoint = "series/observations"
api_endpoint = url + "fred/" + endpoint   # sum of strings
response = requests.get(api_endpoint, params = param_dicts)

response.status_code
content = response.json()
content = content['observations'] # to access value of 'observations' in a content dictionary

df_rgdp = pd.DataFrame(content)
df_rgdp.columns
df_rgdp = df_rgdp[['date', 'value']]


# Unemployment rate
param_dicts = {
  'api_key': 'YOUR_FRED_API_KEY', ## Change to your own key
  'file_type': 'json',
  'series_id': 'UNRATE'    ## ID for US unemployment rate
}
url = "https://api.stlouisfed.org/"
endpoint = "series/observations"
api_endpoint = url + "fred/" + endpoint   # sum of strings
response = requests.get(api_endpoint, params = param_dicts)

response.status_code
content = response.json()
content = content['observations'] # to access value of 'observations' in a content dictionary

df_unemp = pd.DataFrame(content)
df_unemp = df_unemp[['date', 'value']]


df = df_rgdp.merge(df_unemp, on = 'date', how = 'left')
df.columns
df.columns = ['date', 'real_gdp', 'unemployment_rate']

df = df[~df['unemployment_rate'].isna()]




# %%
# =============================================================================
# This section is intentionally left blank
# =============================================================================
