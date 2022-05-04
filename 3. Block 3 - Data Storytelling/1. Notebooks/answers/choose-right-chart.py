books_plotter = (
    books
    .groupby(['Year', 'Genre'])
    .agg(**{'Total Reviews': pd.NamedAgg(column='Reviews',aggfunc='sum'),
            'better_sales': pd.NamedAgg(column='Reviews', aggfunc = lambda col: (col>50_000).sum())})
    .unstack()
)

fig, ax = plt.subplots(figsize=(12,7))

books_plotter.plot(y='Total Reviews', kind='barh',
                   title='Year on year reviews for the 50 Best selling books',
                   xlabel='', width=0.8, color=['#ff9900', '#000000'],
                   ax=ax)

# Grab the years where books had more than 50,000 reviews and get number of books
better_sale_years = books_plotter.loc[books_plotter['better_sales'].sum(axis=1)>0, 'better_sales'].sum(axis=1)

# Add text to show which years where books went above the 50,000 review mark
for ind,num_books in enumerate(better_sale_years):
    text = f'* {num_books}'
    ax.text(-45_000, ind , text, color='#146EB4', weight='bold')

# Explain the *numbers
ax.text(600_000, 0, '* Number of books that received \nover 50,000 reviews that year', color='#146EB4', weight='bold')

# Add the amazon logo
im = plt.imread('images/amazon.png') # insert local path of the image.
newax = fig.add_axes([0.75,0.63,0.4,0.4], anchor='NE', zorder=1)
newax.imshow(im)
newax.axis('off');