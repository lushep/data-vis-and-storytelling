interval = alt.selection_interval(encodings=['x'])
alt.Chart(cars).mark_circle().encode(
    x='Weight_in_lbs',
    y='Miles_per_Gallon',
    color=alt.condition(interval, 'Origin', alt.value('lightgray')),
    tooltip=['Name', 'Year']
).properties(selection=interval, height=300, width=400)