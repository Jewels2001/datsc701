### September 23, 2024
### By: Julie Wojtiw-Quo
"""
Exploring the ACES Montreal 2023 data set -
October 16, 2023 - October 21, 2023 inclusive [6 days]
"""


import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd



day1_df = pd.read_csv("ACES_Montreal_2023/ACES_Montreal_2023/sync_data_calibrated_2023-10-16.csv")

print(day1_df.head())

print(day1_df.columns.to_list())

geometry = gpd.points_from_xy(day1_df.lon, day1_df.lat)

geo_day1_df = gpd.GeoDataFrame(day1_df[['co2d']], geometry=geometry)

print(geo_day1_df.head())

geo_day1_df.plot()
plt.show()
plt.savefig()
