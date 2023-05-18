import pandas as pd

df = pd.read_excel('Lasso Result.xlsx')

zero_cols = df.columns[(df == 0).any()]
df = df.drop(zero_cols, axis=1)
df.to_excel('NewLassoResultCleanIT.xlsx', index=False)
