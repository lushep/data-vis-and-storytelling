import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

# subplot 1
(
    banking
    .groupby('geography')
    ['balance']
    .mean()
    .plot(kind='bar', ax=ax1, 
          color='r',
          title='Salary of customer split by Country')
)

# subplot 2
(
    banking
    .groupby('geography')
    ['age']
    .mean()
    .plot(kind='bar', ax=ax2, 
          color='g',
          title='Age of customer split by Country')
)

# use to separate graphs slightly
fig.tight_layout()