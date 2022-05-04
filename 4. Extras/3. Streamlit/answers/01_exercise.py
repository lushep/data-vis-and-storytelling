import pandas as pd 
import streamlit as st 
import matplotlib.pyplot as plt

chickweight = pd.read_csv('data/chickweight.csv').rename(columns=str.lower)

# add title
st.title("Chicken weight over time by diet")

# set min/max time
min_time = chickweight['time'].min()
max_time = chickweight['time'].max()

(time_start, time_end) = st.sidebar.slider('Time', 
                                            min_value=min_time, 
                                            max_value=max_time, 
                                            value=(min_time, max_time))

# create diet check box
diet = st.sidebar.multiselect(
    'Select diet',
    chickweight['diet'].unique()
)

# filter data
filtered = (
    chickweight
    .loc[lambda df: (df['time'] <= time_end) 
                  & (df['time'] >= time_start)]
    .loc[lambda df: df['diet'].isin(diet)]
)

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

st.pyplot(fig)