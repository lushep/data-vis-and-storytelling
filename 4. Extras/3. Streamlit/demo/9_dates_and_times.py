# Run in terminal with streamlit run 9_dates_and_times.py
import streamlit as st
import pandas as pd
from datetime import datetime, time

DATA_FILEPATH = 'data/uber-raw-data-sep14.csv.gz'

# Write title in main view. 
st.title('NYC Uber Pick-ups Demo')
st.write('Simple demo to illustrate the usefulness of `st.cache` and the use of `st.map`.')

# Use st.cache decorator to prevent re-loading the data.
@st.cache
def load_data(nrows):
    data = (
        pd.read_csv(DATA_FILEPATH, nrows=nrows)
        .rename(str.lower, axis='columns')
    )
    data['date/time'] = pd.to_datetime(data['date/time'])
    return data

# Load the data. 
data = load_data(100000)
first_date = data['date/time'].min()
last_date = data['date/time'].max()

# Controls. 
st.sidebar.markdown('# Controls')
date = st.sidebar.date_input('Date', min_value=first_date, max_value=last_date, value=first_date)
(time_start, time_end) = st.sidebar.slider('Time', value=(time(9, 00), time(12, 30)))


# Filter data. 
data = (
    data
    .loc[lambda d: d['date/time'].dt.date == date]
    .loc[lambda d: d['date/time'].dt.time >= time_start] 
    .loc[lambda d: d['date/time'].dt.time <= time_end]
)

# Create a map. The Pandas dataframe must contain a lat and lon column. 
st.map(data)

# Add checkbox.
if st.sidebar.checkbox('Show raw data'): 
    st.write(data)
