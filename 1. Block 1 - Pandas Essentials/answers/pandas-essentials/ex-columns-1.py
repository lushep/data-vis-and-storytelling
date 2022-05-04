(
    banking
    .assign(good_credit = lambda df: df['creditscore']>800)
    .loc[:, 'good_credit']
    .mean()
)
# 6.36% of the customer base have good credit