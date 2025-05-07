#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  7 10:32:13 2025

@author: bchoe
"""

import pandas as pd
fortune1000 = pd.read_csv("https://bcdanl.github.io/data/fortune1000_2024.csv")

fortune = fortune1000[[
    "Rank", "Company", "Sector", "Industry",
    "Revenues_M", "Profits_M", "Number_of_Employees"
]]


sector_and_industry = fortune.groupby(['Sector', 'Industry'])
sector_and_industry
len(sector_and_industry)


df_sum = sector_and_industry.describe()


agg_tbl = (
    fortune
    .groupby(["Sector", "Industry"]) # this must be a list
    .agg(
        n_companies = ("Company",   "size"),
        avg_rev     = ("Revenues_M","mean"),
        tot_rev     = ("Revenues_M","sum")
    )
    .reset_index()  # Flattens the MultiIndex into ordinary columns
)


fortune['pct_of_industry_rev'] = (
        fortune
        .groupby(["Sector", "Industry"])["Revenues_M"]
        .transform(lambda x: 100 * x / x.sum() )
)


def above_median(df):
    med = df["Revenues_M"].median()
    return df[ df["Revenues_M"] > med ]      

df = (
    fortune
    .groupby(["Sector", "Industry"])
    .apply(above_median)      
)




# %%
# =============================================================================
# Classwork 14
# =============================================================================

# 

import pandas as pd
import numpy as np
beer = pd.read_csv('https://bcdanl.github.io/data/beer_markets.csv')


# Q1. 
# What are the descriptive statistics (mean, count, min, max) 
# for dollar_spent and beer_floz grouped by brand?


q1_dollar_spent = (
      beer
      .groupby('brand')['dollar_spent']
      .describe()
      )


q1_beer_floz = (
      beer
      .groupby('brand')['beer_floz']
      .describe()
      )

# Q2
# For each market, find the average price_per_floz, total dollar_spent, and total beer_floz.
# Which market has the highest average price_per_floz?

q2 = (
      beer
      .groupby('market')
      .agg(
          price_per_floz_avg = ('price_per_floz', 'mean'),
          dollar_spent_tot = ('dollar_spent', 'sum'),
          beer_floz_tot = ('beer_floz', 'sum')
          )
      .sort_values('price_per_floz_avg', ascending = False)
      )




# Q3
# For each brand, calculate the percentage contribution of dollar_spent 
# on the same brand to the total dollars spent by the household.


q3 = (
      beer
      .groupby(['hh', 'brand'])
      .agg(dollar_spent_per_brand = ('dollar_spent', 'sum'))
      )

q3['dollar_spent_tot'] = q3.groupby('hh')['dollar_spent_per_brand'].transform('sum')

q3['dollar_spent_pct'] = q3['dollar_spent_per_brand'] / q3['dollar_spent_tot']


# Q4

q4 = (
      beer
      .groupby('market')
      .apply(lambda df: df.nlargest(1, 'price_per_floz', keep = 'all'))
      )



# Q5
# Among households that have purchased BUD LIGHT at least once, 
# what proportion only bought BUD LIGHT?

# (proportion) = (# hh that purchased only BUD) / (# hh that purchased BUD at least once)


q5_bud = (
    beer[beer['brand'] == 'BUD LIGHT'][['hh']]
    .drop_duplicates()
    ) 

len(q5_bud) # hh that purchased BUD at least once

q5_bud_loyal = (
    beer[beer['hh'].isin(q5_bud['hh'])][['hh', 'brand']]
    .value_counts()
    .reset_index()['hh']
    .value_counts()
    .reset_index()
    .query('count == 1')
    )

len(q5_bud_loyal)

100 * len(q5_bud_loyal) / len(q5_bud)


def loyal(brand_beer):
    q5_brand_beer = (
        beer[beer['brand'] == brand_beer][['hh']]
        .drop_duplicates()
        ) 

    q5_brand_beer_loyal = (
        beer[beer['hh'].isin(q5_brand_beer['hh'])][['hh', 'brand']]
        .value_counts()
        .reset_index()['hh']
        .value_counts()
        .reset_index()
        .query('count == 1')
        )

    return 100 * len(q5_brand_beer_loyal) / len(q5_brand_beer)

# beer['brand'].unique()

lst = []
for item in beer['brand'].unique():
    print(item, loyal(item))    
    lst.append({
        'brand': item,
        'loyal_pct': loyal(item)
        })

pd.DataFrame(lst).nlargest(1, 'loyal_pct')




# %%
# =============================================================================
# 
# =============================================================================
