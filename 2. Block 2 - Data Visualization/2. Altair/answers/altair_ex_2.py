alt.Chart(cars).mark_point(
    size = 100
).encode(
    x='Acceleration',
    y='Weight_in_lbs',
    color='Cylinders:O',
    shape='Origin',
    tooltip=['Name']
)

# Bonus: 
alt.Chart(cars).mark_point(
    size = 100
).encode(
    x='Acceleration',
    y='Weight_in_lbs',
    color='Cylinders:N',
    shape='Origin',
    tooltip=['Name']
)