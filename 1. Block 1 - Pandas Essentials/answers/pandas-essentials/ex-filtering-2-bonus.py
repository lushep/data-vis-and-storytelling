## BONUS ##
banking.loc[lambda df: df['surname'].str.startswith('Mill'), 'surname'].unique()
# the names are ['Mills', 'Miller', 'Millar', 'Milligan', 'Milliner']