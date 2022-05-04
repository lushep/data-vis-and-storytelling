# Run in terminal with streamlit run pandas.py
import streamlit as st
import pandas as pd

DATA_FILEPATH = 'data/chickweight.csv'
# Write title in main view. 
st.write('# Chickweight dataset')

def load_data():
    ''' Loads chickweight dataset. '''
    return (
    pd.read_csv(DATA_FILEPATH)
    .rename(str.lower, axis='columns')
)
chickweight = load_data()

# Select diet in the sidebar: one option to select.
diet = st.sidebar.selectbox(
    'Select diet', 
    chickweight['diet'].unique()
)

# Select columns in the sidebar: can select multiple.
columns = st.sidebar.multiselect(
    'Select column',
    chickweight.columns
)

# Filter chickweight based on selection. 
filtered_chickweight = (
    chickweight
    .loc[lambda d: d['diet'] == diet]
    .loc[:, columns]
)

# Display filtered chickweight in main view.
st.write(filtered_chickweight)
