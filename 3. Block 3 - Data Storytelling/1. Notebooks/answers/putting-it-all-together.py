new_companies = ['Josie Saws', 'Golden Kez Topic', 'Samuelifant Graveyard']

low_c = '#ff5100'
high_c = 'lightseagreen'

sales_plot = (
    sales
    .assign(Sales = lambda df: df['Sales']/1000,
            benchmark = lambda df: df['Sales'].mean()*0.9,
            over_benchmark = lambda df: df['Sales'] >= df['benchmark'],
            color = lambda df: df['over_benchmark'].map({True: high_c, False:low_c}),
            new_comp = lambda df: df['Company'].isin(new_companies)
           )
)

# Create necessary variables for adding to plot
max_x = sales_plot['Sales'].max()
report_year = pd.Timestamp('today').year - 1
report_previous_year = report_year - 1


#### Now create the plot ####

fig, ax = plt.subplots(figsize=(12,7))
plt.barh(sales_plot['Company'], sales_plot['Sales'], color=sales_plot['color'])

ax.tick_params(axis='x', labelrotation = 45)

# Style: set the xlim and add good labels
ax.set(xlim=[-10, max_x*1.01], 
       xlabel='Total Revenue', 
       ylabel='Company', 
       title=f'Revenue by Company {report_year} Compared to {report_previous_year}')

# Add a vertical line for benchmark, here we set the style in the function call
ax.axvline(benchmark, ls='--', color='k')
ax.text(benchmark*1.02, 0.8, 'Benchmark', fontsize=10, color='k')

# Annotate new companies
for group in sales_plot.index[sales_plot['new_comp']]:
    ax.text(max_x*1.02, group, "New Company", fontsize=10,
            verticalalignment="center")