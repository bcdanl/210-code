#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 10:15:21 2026

@author: bchoe
"""

# %%
# =============================================================================
# NYC Open Data
# =============================================================================
# https://data.cityofnewyork.us/resource/k397-673e.json


import requests
import pandas as pd

endpoint = 'https://data.cityofnewyork.us/resource/k397-673e.json'  ## API endpoint
response = requests.get(endpoint)

content = response.json() # to convert JSON response data to a dictionary/ a list of dicts
df = pd.DataFrame(content)


# %%
# =============================================================================
# FRED APIs
# =============================================================================


import requests  # to handle API requests
import json      # to parse JSON response data
import pandas as pd
param_dicts = {
  'api_key': '80657885ed24a6137d5f63590c0e5c4a', ## Change to your own key
  'file_type': 'json',
  'series_id': 'GDPC1'    ## ID for US real GDP
}
url = "https://api.stlouisfed.org/"
endpoint = "series/observations"
api_endpoint = url + "fred/" + endpoint   # sum of strings
response = requests.get(api_endpoint, params = param_dicts)

# Convert JSON response to Python dictionary.
content = response.json()

content.keys()
content.values()

tmp = content['observations']

# Extract the "observations" list element.
df = pd.DataFrame( tmp )

df.info() # object in Dtype means string


# %%
# =============================================================================
# Classwork 9
# =============================================================================
# Question 1. NYC Open Data API

import requests
import pandas as pd

endpoint = 'https://data.cityofnewyork.us/resource/c3uy-2p5r.json'  ## API endpoint

# query parameters (e.g., limit rows)
param_dict = {
    "$limit": 100   # You can increase this to get more observations
}

response = requests.get(endpoint,
                        params= param_dict)

content = response.json() # to convert JSON response data to a dictionary/ a list of dicts


df = pd.DataFrame(content)



# %%
# =============================================================================
# Classwork 9
# =============================================================================
# Question 2. FRED API


import requests  # to handle API requests
import pandas as pd
param_dicts = {
  'api_key': 'YOUR_API_KEY', ## Change to your own key
  'file_type': 'json',
  'series_id': 'GDPC1'    ## ID for US real GDP
}

# How we can update a value for a corresponding key, 'series_id'
param_dicts['series_id'] = 'UNRATE'
param_dicts

url = "https://api.stlouisfed.org/"
endpoint = "series/observations"
api_endpoint = url + "fred/" + endpoint   # sum of strings


response = requests.get(api_endpoint, params = param_dicts)

# Convert JSON response to Python dictionary.
content = response.json()

content.keys()
content.values()

tmp = content['observations']

# Extract the "observations" list element.
df = pd.DataFrame( tmp )



# Answer:
import requests  # to handle API requests
import pandas as pd

param_dicts = {
  'api_key': 'YOUR_API_KEY', ## Change to your own key
  'file_type': 'json',
  'series_id': 'GDPC1'    ## ID for US real GDP
}

url = "https://api.stlouisfed.org/"
endpoint = "series/observations"
api_endpoint = url + "fred/" + endpoint   # sum of strings

df_all = pd.DataFrame()
series_lst = ['GDPC1', 'UNRATE']

for val in series_lst:
    
    param_dicts['series_id'] = val
    response = requests.get(api_endpoint, 
                            params= param_dicts)
    
    content = response.json()    
    df['series_id'] = val
    df = pd.DataFrame( content['observations'] )

    

















