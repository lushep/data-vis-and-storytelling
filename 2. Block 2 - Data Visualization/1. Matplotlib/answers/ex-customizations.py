x = np.arange(30)
y_linear = x*2
y_quadratic = x**2

fig, ax1 = plt.subplots()

ax1.plot(x, y_linear)

ax2 = ax1.twinx()

ax2.plot(x, y_quadratic, color='orange')

# add legend
fig.legend(['Linear','Quadratic'], loc=(0.65,0.15))

# set ylabels for both axes
ax1.set_ylabel('Linear')
ax2.set_ylabel('Quadratic')

# set title
ax1.set_title('This is my title')

# make the gridlines match up and add only the y gridlines to the axes
ax1.set_yticks(np.linspace(*ax1.get_ybound(), 10))
ax2.set_yticks(np.linspace(*ax2.get_ybound(), 10))
ax1.grid(axis='y')