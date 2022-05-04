import pandas as pd 
import streamlit as st 
import matplotlib.pyplot as plt

chickweight = pd.read_csv('data/chickweight.csv').rename(columns=str.lower)

# add title

# set min/max time

# create diet check box

# filter data

# plot chart
fig, ax = plt.subplots()

(
    filtered
    .groupby(['time','diet'])
    ['weight']
    .mean()
    .unstack()
    .plot(ax=ax)
)

# show chart on streamlit