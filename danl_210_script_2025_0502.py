#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  2 10:35:19 2025

@author: bchoe
"""

import pandas as pd
fortune1000 = pd.read_csv("https://bcdanl.github.io/data/fortune1000_2024.csv")

fortune = fortune1000[[
    "Rank", "Company", "Sector", "Industry",
    "Revenues_M", "Profits_M", "Number_of_Employees"
]]

fortune['Sector'].nunique()

sum_g = fortune.groupby('Sector').describe()


type( fortune.groupby("Sector") )


fortune.groupby("Sector").mean()


fortune.groupby("Sector").max()

fortune.groupby("Sector").size()

type( fortune.groupby("Sector")["Revenues_M"] )

fortune.groupby("Sector")["Revenues_M"].mean()
fortune.groupby("Sector")["Revenues_M"].median()
fortune.groupby("Sector")["Revenues_M"].max()
fortune.groupby("Sector")["Revenues_M"].min()
fortune.groupby("Sector")["Revenues_M"].sum()


fortune.groupby("Sector")["Revenues_M"]  # this is a SeriesGroupBy object
fortune.groupby("Sector")["Revenues_M"].agg('sum')
fortune.groupby("Sector")["Revenues_M"].agg('mean')
fortune.groupby("Sector")["Revenues_M"].agg('max')
fortune.groupby("Sector")["Revenues_M"].agg('min')


df_sum = (
    fortune.groupby("Sector").agg(
  Revenues_M_min = ("Revenues_M", "min"),
  Profit_count = ("Profits_M", "count"),
  Profit_size = ("Profits_M", "size"),
  Profits_M_max = ("Profits_M", "max"),
  Number_of_Employees_mean = ("Number_of_Employees", "mean")
).reset_index()
    )


fortune.info()

fortune.groupby("Sector").agg(sth = ('Revenues_M', 'quantile(.25)'))

fortune.groupby("Sector").agg(
    Revenue_IQR = ("Revenues_M", lambda s: s.quantile(0.75) - s.quantile(0.25) )
)



# %%
# =============================================================================
# Classwork 13
# =============================================================================

cereal = pd.read_csv('https://bcdanl.github.io/data/cereals_oatmeal.csv')

cereal.columns

# Q1
# Group the data by Manufacturer, and 
# determine the number of groups and the number of cereals per group.


len(cereal.groupby('Manufacturer'))

cereal.groupby('Manufacturer').size()


(
 cereal.groupby('Manufacturer').size()
 .reset_index(name = 'count')
 )




# Q2
# Calculate the mean of the Calories, Fiber, and Sugars 
# for every manufacturer.

cereal.info()

q2 = (
 cereal.groupby('Manufacturer')
 .agg(
      Calories_mean = ('Calories', 'mean'),
      Fiber_mean = ('Fiber', 'mean'),
      Sugars_mean = ('Sugars', 'mean'),
      n_obs = ('Name', 'size')
      )
 .reset_index()
)



# Q3
# Create a new DataFrame that includes 
# the maximum Sugars and the minimum Fiber per manufacturer.
 










# %%
# =============================================================================
# transform()
# =============================================================================
fortune.columns


fortune.groupby('Sector')['Revenues_M'].transform('mean')



fortune["Sector_rev_mean"] = (
    fortune.groupby('Sector')['Revenues_M']
    .transform('mean')
    )

fortune["Rev_centered_2"] = fortune["Revenues_M"] - fortune["Sector_rev_mean"]


fortune["Rev_centered"] = (
    fortune.groupby('Sector')['Revenues_M']
    .transform(lambda s: s - s.mean())
    )

sectors = fortune.groupby("Sector")
fortune.columns


fortune_new = fortune.assign(
    Year = 2024,
    nCompanies = sectors['Company'].transform('size'),
    Revenues_M_min = sectors['Revenues_M'].transform('min'),
    Profits_M_max = sectors['Profits_M'].transform('max'),
    Number_of_Employees_mean = sectors['Number_of_Employees'].transform('mean')
)


fortune_2021_2024 = pd.read_csv("https://bcdanl.github.io/data/fortune741_2021_2024.csv")

	Revenues_M
0	648125.0
1	611289.0
2	572754.0
3	523964.0




# %%
# =============================================================================
# Blank Section
# =============================================================================
