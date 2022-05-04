(
    banking
    .loc[lambda df: df['exited']==1]
    .assign(can_vote = lambda df: df['age'] >= 18)
    .groupby('can_vote')
    [['estimatedsalary']]
    .mean()
    .round(2)
)