x = np.linspace(0, 10, 20)
_ = plt.plot(x, x**0.5, 'k-', x, x*0.5, 'go', x, 0.05*x**2, 'r^')