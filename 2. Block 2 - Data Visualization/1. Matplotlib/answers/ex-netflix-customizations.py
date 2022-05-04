fig, ax = plt.subplots(
    figsize=(10,6) # ★★ make the figure larger
) 

netflix_directors.plot(y=['Movie', 'TV Show'], 
                       kind='bar', stacked=True, 
                       ax=ax, 
                       color = ['turquoise', 'pink']) # ★★ set the colors

# ★ add a title
ax.set_title('Plot to show the number of TV Shows and Movies by the top 10 Directors on US Netflix')

# ★ set the y and x labels
ax.set_ylabel('Count')
ax.set_xlabel('Director')

# ★★★ change the yticks to only show integers
ax.yaxis.get_major_locator().set_params(integer=True)
ax.grid(axis='y')

# ★★★ add a horizontal line for the mean of the total
ax.axhline(netflix_directors['total'].mean(), color='k', linestyle='--')