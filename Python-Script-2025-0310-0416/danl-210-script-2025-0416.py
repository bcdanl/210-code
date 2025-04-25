#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 11:00:02 2025

@author: bchoe
"""

# %%
# =============================================================================
# New York Times API using `pynytimes` (Unofficial Python Wrapper)
# =============================================================================

# Settings
import pandas as pd
from pynytimes import NYTAPI

# Initialize API with your key
nyt = NYTAPI("YOUR_NYT_API_KEY", parse_dates=True)


# Top Stories
top_stories = nyt.top_stories()

# Get all the top stories from a specific category
top_climate_stories = nyt.top_stories(section = "climate")


df_top_stories = pd.DataFrame(top_stories)
df_top_climate_stories = pd.DataFrame(top_climate_stories)



# Most Viewed
most_viewed = nyt.most_viewed()

# Get most viewed articles of last 7 or 30 days
most_viewed = nyt.most_viewed(days = 7)
most_viewed = nyt.most_viewed(days = 30)


from datetime import datetime

# Define the date range
start = datetime(2024, 1, 1)
end = datetime(2024, 12, 31)

# Search articles related to climate within a date range
  # This return only up to 10 articles.
articles = nyt.article_search(
    query="climate",
    dates={"begin": start, "end": end},
)



# %%
# =============================================================================
# NYT API with requests methods - Article Search
# =============================================================================
import requests
import time
import pandas as pd
# from datetime import datetime

api_key = "YOUR_NYT_API_KEY"
base_url = "https://api.nytimes.com/svc/search/v2/articlesearch.json"

# Set a broader date range (e.g., all of January 2024)
begin_date = "20240101"
end_date = "20240131"

all_articles = []

for page in range(10):  # up to 100 articles
    params = {
        "q": "climate",
        "begin_date": begin_date,
        "end_date": end_date,
        "page": page,
        "api-key": api_key
    }

    response = requests.get(base_url, params=params)
    if response.status_code != 200:
        print(f"Error on page {page}: {response.text}")
        break

    data = response.json()
    docs = data.get("response", {}).get("docs")

    if docs is None or len(docs) == 0:
        print(f"Page {page} - No articles found.")
        break

    print(f"Page {page} - {len(docs)} articles found.")

    for doc in docs:
        all_articles.append({
            "headline": doc["headline"]["main"],
            "abstract": doc.get("abstract"),
            "pub_date": doc.get("pub_date"),
            "section": doc.get("section_name"),
            "url": doc.get("web_url")
        })

    if len(docs) < 10:
        break  # no more pages

    time.sleep(6)

df = pd.DataFrame(all_articles)
print(f"\nTotal articles collected: {len(df)}")
print(df.head())

# %%

import requests
import pandas as pd
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:137.0) Gecko/20100101 Firefox/137.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://www.premierleague.com',
    'Connection': 'keep-alive',
    'Referer': 'https://www.premierleague.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'Priority': 'u=0',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

params = {
    'page': '1',
    'pageSize': '10',
    'compSeasons': '719',
    'comps': '1',
    'compCodeForActivePlayer': 'EN_PR',
    'altIds': 'true',
}

response = requests.get('https://footballapi.pulselive.com/football/stats/ranked/players/goals', params=params, headers=headers)


content = response.json()
content = content['stats']
content = content['content']


df_content = pd.DataFrame(content)

df_content = pd.json_normalize(content)


# https://footballapi.pulselive.com/football/stats/ranked/players/goals?page=1&pageSize=10&compSeasons=719&comps=1&compCodeForActivePlayer=EN_PR&altIds=true




import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:137.0) Gecko/20100101 Firefox/137.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://www.premierleague.com',
    'Connection': 'keep-alive',
    'Referer': 'https://www.premierleague.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

params = {
    'page': '0',
    'pageSize': '10',
    'compSeasons': '489',
    'comps': '1',
    'compCodeForActivePlayer': 'EN_PR',
    'altIds': 'true',
}

response = requests.get('https://footballapi.pulselive.com/football/stats/ranked/players/goals', params=params, headers=headers)


content = response.json()
content = content['stats']
content = content['content']


df_content = pd.DataFrame(content)

df_content = pd.json_normalize(content)


# %%
# =============================================================================
# HuggingFace's free LLM API
# =============================================================================



import requests
import pandas as pd

# Load the data
imdb = pd.read_csv('YOUR_IMDB_DATA.csv')

# Use the first 2 plot descriptions
plot_data = imdb['plot'].tolist()[:2]

# Combine the plots into a single string
plot_info_text = "\n".join(plot_data)
input_text = f"Characterize plot of top 2 movies:\n{plot_info_text}"

# Hugging Face API setup
HF_API_TOKEN = "YOUR_HUGGINGFACE_API_TOKEN"  # Replace with your token
API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": f"Bearer {HF_API_TOKEN}"}

# Send POST request
payload = {"inputs": input_text}
response = requests.post(API_URL, headers=headers, json=payload)

# Parse and display result
if response.status_code == 200:
    output = response.json()
    summary = output[0]["summary_text"]
    print("\nSummary from Hugging Face Inference API:")
    print(summary)
else:
    print("Unexpected response structure:", output, 'or')
    print(f"\nAPI request failed with status code {response.status_code}:")
    print(response.text)