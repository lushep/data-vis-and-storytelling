# Run in terminal with streamlit run 7_pandas_and_cache.py
import streamlit as st
import pandas as pd

DATA_FILEPATH = 'data/uber-raw-data-sep14.csv.gz'

# Write title in main view. 
st.title('NYC Uber Pick-ups Demo')
st.write('Simple demo to illustrate the usefulness of `st.cache.` and the use of `st.map`.')

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

# Filter the data. 
hour = st.sidebar.number_input('Hour to look at', min_value = 0, max_value = 23, value = 12)
data = data.loc[lambda d: d['date/time'].dt.hour == hour]

# Create a map. The Pandas dataframe must contain a lat and lon column. 
st.map(data)
