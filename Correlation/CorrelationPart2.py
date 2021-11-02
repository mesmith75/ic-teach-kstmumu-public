"""
Correlation between variables Part2
Visualization of correlation

Author: Artem
Date: 02/11
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_pickle("./heatMap.pkl")
columns = df.columns
N = len(columns)
heatMap = df.values

sig_fig = 2
for i in range(N):
    for j in range(N):
        heatMap[i, j] = round(heatMap[i, j], sig_fig)

fig, ax = plt.subplots(figsize = (60, 60))
im = ax.imshow(heatMap)

# We want to show all ticks...
ax.set_xticks(np.arange(N))
ax.set_yticks(np.arange(N))
# ... and label them with the respective list entries
ax.set_xticklabels(columns)
ax.set_yticklabels(columns)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

"""
# Loop over data dimensions and create text annotations.
for i in range(N):
    for j in range(N):
        text = ax.text(j, i, heatMap[i, j],
                       ha="center", va="center", color="w")
"""

ax.set_title("Correlation between colunms")
#fig.tight_layout()
plt.savefig("heatMap_correlation")
plt.show()
