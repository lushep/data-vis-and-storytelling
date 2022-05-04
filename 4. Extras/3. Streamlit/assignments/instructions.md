# Streamlit Exercise

1. Plot a matplotlib chart using the chickweight data
2. Add a title using streamlit
3. Add a slidebar to be able to filter on the time column
4. Add a multiselect checkbox to be able to filter on diet
5. Modularise the code

## 1. Plot

- Add the streamlit command to the `existing_code.py` file to show the chart on your application

## 2. Add a title

- Use the streamlit command to add a title
- Use the streamlit command to add more information to your app.
    - Use as much markdown as you wish

## 3. Add a slidebar for time

- Create variables to store the min and max time (`min_col = df['col'].min()`)
- Use `st.sidebar.slider` with the min and max time to create streamlit variables
- Use the `.loc` method to filter (`df.loc[df['col'] <= min_col`)

## 4. Add a select box for diet

- Use `st.sidebar.multiselect` with the unique diet variables
- Use the `.loc` method to filter (`df.loc[df['col'].isin(list_of_unique_values)`)

## 5. Modularise the code

- Convert all sections of the code to use functions
- Create a main() function that will be run when `streamlit run file.py` is run