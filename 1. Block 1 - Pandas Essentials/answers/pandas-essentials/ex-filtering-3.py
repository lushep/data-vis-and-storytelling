banking.loc[lambda df: (df['exited']==0 )
            & (df['numofproducts']>=3)
            & ( (df['isactivemember']==1) | (df['tenure'] >= 3) )
            & (df['geography']=='Spain')
            & (df['age'] < 25)]

# Just one person (Calzada) is eligible for the Tarjeta Española