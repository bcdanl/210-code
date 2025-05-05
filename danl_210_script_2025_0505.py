#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  5 10:35:57 2025

@author: bchoe
"""
import pandas as pd
f_2021_2024 = pd.read_csv("https://bcdanl.github.io/data/fortune741_2021_2024.csv")


# %%
# =============================================================================
# transform() with shift()
# =============================================================================


f_2021_2024['Revenues_M_last_year'] = (
    f_2021_2024.groupby('Company')['Revenues_M'].shift(-1)
    )

f_2021_2024['Diff_Revenues_M'] = (
    f_2021_2024['Revenues_M'] - f_2021_2024['Revenues_M_last_year']
    )

f_2021_2024['Revenue_Growth_Rate'] = (
    f_2021_2024['Diff_Revenues_M'] / f_2021_2024['Revenues_M_last_year']
    ) 



# %%
# =============================================================================
# apply
# =============================================================================

fortune_shuffled = pd.read_csv("https://bcdanl.github.io/data/fortune1000_2024_shuffled.csv")
sectors = fortune_shuffled.groupby("Sector")

sectors.nlargest(3, 'Revenues_M')
# AttributeError: 'DataFrameGroupBy' object has no attribute 'nlargest'

sectors.sort_values('Revenues_M')
# AttributeError: 'DataFrameGroupBy' object has no attribute 'sort_values'

top3_per_sector = sectors.apply(lambda df: df.nlargest(3, 'Revenues_M', keep = "all"))


top3_per_sector = (
    sectors.apply(lambda df: df.nlargest(3, 'Revenues_M', keep = "all"))
    .reset_index(drop=True)
    )


def get_nlargest_obs(df, n, var):
    return df.nlargest(n, var, keep="all")

sectors.apply(get_nlargest_obs)
# TypeError: get_nlargest_obs() missing 2 required positional arguments: 'n' and 'var'


top5_profit = sectors.apply(get_nlargest_obs, 5, 'Profits_M')


def filter_by_threshold(df, column, threshold):
    return df[ df[column] > threshold ]

sectors.apply(filter_by_threshold, "Revenues_M", 5000)



# %%
# =============================================================================
# CLASSWORK 13 - Q3-Q6
# =============================================================================

cereal = pd.read_csv('https://bcdanl.github.io/data/cereals_oatmeal.csv')
cereal.columns


# Q3
# Create a new DataFrame that includes 
# the maximum Sugars and the minimum Fiber per manufacturer.

q3 = (
      cereal
      .groupby('Manufacturer')
      .agg(
          Sugars_max = ('Sugars', 'max'),
          Fiber_min = ('Fiber', 'min')
          )
      )

# Q4

g = cereal.groupby('Manufacturer')

cereal['Normalized_Sugars'] = (
   ( cereal['Sugars'] - g['Sugars'].transform('mean') ) / 
           g['Sugars'].transform('std')
    )


# Q5
# Put the two highest-sugar cereals for every manufacturer in a new DataFrame.

q5 = (
      cereal
      .groupby('Manufacturer')
      .apply(lambda df: df.nlargest(2, 'Sugars', keep = 'all'))
      )

# Q6
cereal["Calories"].corr( cereal["Sugars"] ) # returns a correlation value


cereal[["Calories", "Sugars"]].corr() # returns a DataFrame of correlation matrix


cereal[["Calories", "Sugars", "Fiber"]].corr() # returns a DataFrame of correlation matrix

q6 = (
      cereal
      .groupby('Manufacturer')
      .apply(lambda df: df['Calories'].corr( df['Sugars'] ))
      .reset_index()
      )




# %%
# =============================================================================
# BLANK
# =============================================================================
