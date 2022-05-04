(
    banking
    .groupby('geography')
    [['age']]
    .mean()
    .round(2)
)