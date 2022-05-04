(
    banking
    .assign(can_vote = lambda df: df['age'] >= 18)
    .groupby('can_vote')
    [['estimatedsalary']]
    .mean()
    .round(2)
)