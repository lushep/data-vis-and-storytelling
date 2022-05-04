import pandas as pd 
import streamlit as st 
import matplotlib.pyplot as plt

# set filepath
FILE_PATH = 'data/chickweight.csv'

# add title
st.title("Chicken weight over time by diet")

def read_data(path=FILE_PATH, lower_cols = True):
    df = pd.read_csv('data/chickweight.csv')

    if lower_cols:
        df = df.rename(columns=str.lower)

    return df

# set min/max time
def get_min_max(df, col='time'):
    min_col = df[col].min()
    max_col = df[col].max()

    return st.sidebar.slider(col.title(), 
                                            min_value=min_col, 
                                            max_value=max_col, 
                                            value=(min_col, max_col))

# create diet check box
def get_checkbox(df, col='diet'):
    return st.sidebar.multiselect(
        'Select diet',
        df['diet'].unique()
    )

# filter data
def filter_slider(df, col, start, end):
    return (
        df
        .loc[lambda df: (df[col] <= end) 
                    & (df[col] >= start)]
    )

def filter_multiselect(df, col, vals):
    return df.loc[lambda df: df[col].isin(vals)]

# plot chart
def plot_agg(df, ax):

    (
        df
        .groupby(['time','diet'])
        ['weight']
        .mean()
        .unstack()
        .plot(ax=ax)
    )


def main():

    chickweight = read_data()
    time_start, time_end =  get_min_max(df=chickweight)
    diet_vals = get_checkbox(df=chickweight)
    filtered = (
        chickweight
        .pipe(filter_slider, col='time', start=time_start, end=time_end)
        .pipe(filter_multiselect, col='diet', vals=diet_vals)
    )
    fig, ax = plt.subplots()
    plot_agg(filtered, ax=ax)
    st.pyplot(fig)

    st.write(time_start, diet_vals, filtered)


if __name__ == '__main__':
    main()