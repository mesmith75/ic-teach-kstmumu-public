"""
Try box-and-wiskers plot to identify background vs signal

Author : Artem
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

root = "C:/Users/Abelo/Desktop/Docs/University/Year3/TBPS/data/"
files = ["total_dataset", "acceptance_mc", "jpsi", "jpsi_mu_k_swap", "jpsi_mu_pi_swap", "k_pi_swap", \
         "phimumu", "pKmumu_piTop", "pKmumu_piTop", "psi2S", "sig"]
ext = ".pkl"

bin_ranges = ["0.1_0.98", "1.1_2.5", "2.5_4.0", "4.0_6.0", "6.0_8.0", "15.0_17.0", "17.0_19.0", "11.0_12.5",\
              "1.0_6.0", "15.0_17.9"]


def read_range(vals):
    lims = vals.split("_")
    return float(lims[0]), float(lims[1])


dfs = []
for file in files:
    dfs.append(pd.read_pickle(root + file + ext))

columns = dfs[0].columns

col = ["red", "green", "blue", "orange", "purple", "tan", "cyan", "forestgreen", "gold", "crimson", "sienna", "salmon", "darkred", "lightcoral"]
for k, column in enumerate(columns):
    print("Starting column #", k)
    fig, ax = plt.subplots(len(bin_ranges), 1, figsize = (20, 160))
    plt.title("Distribution for " + column)

    for i, bin_r in enumerate(bin_ranges):
        #print("Starting bin ", i)
        dfs_2 = []
        for df in dfs:
            lims = read_range(bin_r)
            dfs_2.append(df[(df["q2"] > lims[0]) & (df["q2"] < lims[1])][column])
        ax[i].set_title("Bin of q2: " + bin_r)
        boxes = []
        for j, df in enumerate(dfs_2):
            #print("Operating with df ", j)
            #ax[i].boxplot(df, label = files[j])
            bx = ax[i].boxplot([float(val) for val in df], vert = False, patch_artist = True, \
                               positions = [j], boxprops=dict(facecolor=col[j], color=col[j]))
            boxes.append(bx)
        ax[i].legend([box["boxes"][0] for box in boxes], files, loc = "upper right")

    Path(root + "output_box/").mkdir(parents=True, exist_ok=True)
    plt.savefig(root + "output_box/" + column)
    plt.clf()













