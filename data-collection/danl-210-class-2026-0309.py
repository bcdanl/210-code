#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 09:53:17 2026

@author: bchoe
"""

import requests  # to handle API requests
import json      # to parse JSON response data
import pandas as pd
param_dicts = {
  'api_key': 'YOUR_API_KEY', ## Change to your own key
  'file_type': 'json',
  'series_id': 'GDPC1'    ## ID for US real GDP
}

url = "https://api.stlouisfed.org/"
endpoint = "series/observations"
api_endpoint = url + "fred/" + endpoint   # sum of strings
response = requests.get(api_endpoint, params = param_dicts)

# Convert JSON response to Python dictionary.
content = response.json() 

# Extract the "observations" list element.
df = pd.DataFrame( content['observations'] )



# %%
# =============================================================================
# Classwork 9 - Question 2
# =============================================================================

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

lst_series = ['GDPC1', 'UNRATE']
df_all = pd.DataFrame()
for val in lst_series:
    
    param_dicts['series_id'] = val
    response = requests.get(api_endpoint, 
                            params = param_dicts)

    # Convert JSON response to Python dictionary.
    content = response.json() 

    # Extract the "observations" list element.
    df = pd.DataFrame( content['observations'] )
    df['series'] = val
    
    df_all = pd.concat([df_all, df], ignore_index=True)

df_all.columns

# df[ LIST ]
df_all = df_all[ ['date', 'value', 'series'] ]




# %%
# =============================================================================
# NY Times API
# =============================================================================


# Settings
from pynytimes import NYTAPI

# Initialize API with your key
nyt = NYTAPI("YOUR_API_KEY", 
             parse_dates=True)


# Top Stories
top_stories = nyt.top_stories()
df_top_stories = pd.json_normalize(top_stories)



# Get all the top stories from a specific category
top_climate_stories = nyt.top_stories(section = "climate")
df_top_climate_stories = pd.json_normalize(top_climate_stories)


# Most Viewed
most_viewed = nyt.most_viewed()
df_most_viewed = pd.json_normalize(most_viewed)

# Get most viewed articles of last 7 or 30 days
most_viewed_week = nyt.most_viewed(days = 7)
most_viewed_month = nyt.most_viewed(days = 30)


from datetime import datetime

# Define the date range()
start = datetime(2025, 1, 1)
end = datetime(2026, 2, 28)

# Search articles related to climate within a date range
# This returns only up to 10 articles.
articles = nyt.article_search(
    query="climate",
    dates={"begin": start, 
           "end": end},
)

df_articles = pd.json_normalize(articles)


# %%
# =============================================================================
# Hidden API
# =============================================================================
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:148.0) Gecko/20100101 Firefox/148.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Referer': 'https://www.premierleague.com/',
    'Origin': 'https://www.premierleague.com',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
}

response = requests.get(
    'https://cdn-ukwest.onetrust.com/consent/cdf436a9-4615-4772-a4b4-7660a91cc3a2/0198a306-4c89-7808-ab6b-7d1b399c2568/en.json',
    headers=headers,
)

content = response.json()
content.keys()
content['DomainData']


# %%
# =============================================================================
# Premier League Hidden API
# =============================================================================

import requests  
import pandas as pd  
import time
import random 

# Custom headers for browser information
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:137.0) Gecko/20100101 Firefox/137.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://www.premierleague.com',
    'Connection': 'keep-alive',
    'Referer': 'https://www.premierleague.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'Priority': 'u=0'
}

# Query parameters to paginate and filter the player-goals ranking endpoint
params = {
    'page': '0',                          # which page of results to fetch
    'pageSize': '10',                     # how many records per page
    'compSeasons': '719',                 # season identifier (e.g., 2024–25)
    'comps': '1',                         # competition ID (Premier League)
    'compCodeForActivePlayer': 'EN_PR',   # competition code for active players
    'altIds': 'true',                     # include alternative player IDs
}

# Send GET request to the Premier League stats API
response = requests.get(
    'https://footballapi.pulselive.com/football/stats/ranked/players/goals',
    params=params,
    headers=headers
)

# Parse the JSON response into a Python dict
content = response.json()

# Extract the stats dictionary from the content dictionary
stats = content['stats']

# Extract the list of player records from the stats dictionary
goals = stats['content']

# Convert the list of dicts, golas, into a pandas DataFrame for analysis
df_content = pd.json_normalize(goals)

# Sleep for a random 1–2 second interval.
time.seelp(random.uniform(1,2))

# At this point, df_content contains one row per player-goal record,
# with columns for player identifiers, goal counts, team info, etc.
