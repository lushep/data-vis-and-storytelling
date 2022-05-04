import numpy as np

np.diff(
    banking
    .assign(
        savings_this_year = lambda df: df['estimatedsalary']*0.15,
        balance_end_of_year = lambda df: df['balance'] + df['savings_this_year']
    )
    .loc[lambda df: df['exited']==0, ['balance', 'balance_end_of_year']]
    .mean()
).round(2)

# the average balance is expected to increase by 15018.59