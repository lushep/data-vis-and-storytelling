def mark_new_company(df, new_comps):
    """Marks new companies with True/False"""
    return df.assign(new_comp = df['Company'].isin(new_comps))

def convert_to_ms(df, column='Sales', divider=1000):
    """Divides column to convert to millions. Default is 1000s to 1000,000s (/1000)"""
    return df.assign(Sales = df['Sales']/divider)

def compare_to_benchmark(df, column='Sales', benchmark='mean', low_c='r', high_c='b', last_yr = 0.9):
    """Sets a cut-off based as a percentage of an aggregation of a column
    Returns both the transformed data and the benchmark value
    """
    benchmark = df[column].agg(benchmark)*last_yr
    mapping = {True: high_c, False: low_c}
    return df.assign(color = (df[column]>=benchmark).map(mapping)), benchmark

# Identify new companies
new_comps = ['Josie Saws', 'Golden Kez Topic', 'Samuelifant Graveyard']

# Apply transformations
sales_plot, benchmark = (
    sales
    .pipe(convert_to_ms)
    .pipe(mark_new_company, new_comps = new_comps)
    .pipe(compare_to_benchmark, low_c = '#ff5100', high_c = 'lightseagreen')
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