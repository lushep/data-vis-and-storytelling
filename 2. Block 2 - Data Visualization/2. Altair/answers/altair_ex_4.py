# Question 1: 
usa_cars = cars.loc[lambda d: d['Origin'] == 'USA']
interval = alt.selection_interval(encodings=['x', 'y']) 
all_chart = alt.Chart(cars).mark_point().encode(
    x='Horsepower', 
    y='Miles_per_Gallon', 
    color=alt.condition(interval, 'Origin', alt.value('lightgray'))
).properties(selection=interval).interactive()

usa_chart = alt.Chart(usa_cars).mark_point().encode(
    x='Horsepower', 
    y='Miles_per_Gallon', 
    color=alt.condition(interval,'Origin', alt.value('lightgray'))
).properties(selection=interval)

usa_chart | all_chart

# Question 2 
usa_cars = cars.loc[lambda d: d['Origin'] == 'USA']
japan_cars = cars.loc[lambda d: d['Origin'] == 'Japan']
europe_cars = cars.loc[lambda d: d['Origin'] == 'Europe']

all_chart = alt.Chart(cars).mark_point().encode(x='Horsepower', y='Miles_per_Gallon', color='Origin')
usa_chart = alt.Chart(usa_cars).mark_point().encode(x='Horsepower', y='Miles_per_Gallon', color='Origin')
japan_chart = alt.Chart(japan_cars).mark_point().encode(x='Horsepower', y='Miles_per_Gallon', color='Origin')
europe_chart = alt.Chart(europe_cars).mark_point().encode(x='Horsepower', y='Miles_per_Gallon', color='Origin')

all_chart & japan_chart | usa_chart & europe_chart

# Question 3
base_chart = alt.Chart(cars).mark_point().encode(
    y='Miles_per_Gallon',
    color='Origin',
    tooltip=['Name', 'Year']
).interactive()

base_chart.encode(x='Weight_in_lbs') & base_chart.encode(x='Horsepower') | base_chart.encode(x='Acceleration') & base_chart.encode(x='Displacement')