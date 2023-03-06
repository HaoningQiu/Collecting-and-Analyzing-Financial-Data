# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 11:31:43 2021

@author: Edward
"""
import sys
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
Data= pd.read_csv('scraped-data-1.csv')
Data["City"] = "Other"
Data["City"] = np.where(Data["Location"].str.contains("San Francisco"), "San Francisco", Data["City"])
Data["City"] = np.where(Data["Location"].str.contains("Greater Boston"), "Boston", Data["City"])
Data["City"] = np.where(Data["Location"].str.contains("Greater Seattle"), "Seattle", Data["City"])
Data["City"] = np.where(Data["Location"].str.contains("Greater New York"), "New York City", Data["City"])
Data["IsPublic"] = (Data["IPO"].str.contains("Public")).astype(int)
Data["IsHealth"] = (Data["Categories"].str.contains("Health")).astype(int)
Data["IsFin"] = (Data["Categories"].str.contains("Fin")).astype(int)
Data["Year Founded"] = [f[-4:] for f in Data["Founded"].values.tolist()]
Data["Year Founded"] = np.where(Data["Year Founded"].str.contains("20"),Data["Year Founded"].values, np.nan).astype(float)
Data = Data[(Data['Year Founded'] >= 2005) & (Data['Year Founded'] <= 2017)]
print(Data.groupby(['City'])['IsPublic'].mean().reset_index())
print(Data.groupby(['IsHealth'])['IsPublic'].mean().reset_index())
print(Data.groupby(['IsFin'])['IsPublic'].mean().reset_index())

