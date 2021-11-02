"""
Correlation between variables Part1
Creating a pkl of correlation to visualize later

Author: Artem
Date: 02/11
"""

from scipy.stats import pearsonr
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

path = "data/total_dataset.pkl"

data = pd.read_pickle(path)

columns = data.columns
N = len(columns)
heatMap = np.zeros((N, N))

for i, column in enumerate(columns):
    for j, row in enumerate(columns):
        try:
            corr, _ = pearsonr(data[column], data[row])
        except:
            print("Problem with finding correlation between row", j, " and column", i)
            corr = -2
        heatMap[i, j] = corr

df = pd.DataFrame(heatMap, columns, columns)
df.to_pickle("./heatMap.pkl")