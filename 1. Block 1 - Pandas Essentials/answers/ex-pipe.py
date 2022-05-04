# functions
def remove_unwanted_cols(df, cols):
    return df.drop(columns = cols)

def create_can_vote(df, col='age', age=18):
    return df.assign(can_vote = lambda df: df[col] >= age)

def filter_exited_voters(df, col_vote='can_vote', col_exited='exited'):
    return df.loc[lambda df: (df[col_vote]) & (df[col_exited]==1)]

# pipe together
(
    banking
    .pipe(remove_unwanted_cols, cols=['customerid', 'surname'])
    .pipe(create_can_vote)
    .pipe(filter_exited_voters)
)