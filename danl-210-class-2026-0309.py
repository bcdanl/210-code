#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 11:17:49 2026

@author: bchoe
"""

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