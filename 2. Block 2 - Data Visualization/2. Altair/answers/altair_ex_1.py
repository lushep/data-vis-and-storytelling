alt.Chart(cars).mark_point(
    color='green',
    opacity=.4,
    size = 50
).encode(
    x='Acceleration',
    y='Weight_in_lbs',
)