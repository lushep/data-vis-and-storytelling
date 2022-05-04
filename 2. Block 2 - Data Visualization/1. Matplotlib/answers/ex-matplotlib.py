x = np.arange(31)
y1 = x*5 + 50
y2 = 30 - x

plt.figure()
plt.plot(x, y1, color='fuchsia')
plt.title('This is the Fuchsia one')

plt.figure()
plt.plot(x, y2, color='limegreen')
plt.title('This is the Lime Green one')