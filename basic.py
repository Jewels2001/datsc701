
import pandas as pd
import matplotlib as mlp
from matplotlib import pyplot as plt




day1_df = pd.read_csv("ACES_Montreal_2023/ACES_Montreal_2023/sync_data_calibrated_2023-10-16.csv")

test_norm = mlp.colors.Normalize(vmin=-1)

plt.scatter(day1_df['lat'], day1_df['lon'], s=day1_df['co2d'], c=day1_df['co2d'])
plt.colorbar()
plt.show()
#plt.savefig()