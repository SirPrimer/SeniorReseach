import pandas as pd

df = pd.read_excel('LassoResultClean.xlsx', index_col=0)

df_transposed = df.transpose()

df_transposed.to_excel('LassoResultClean_transposed.xlsx')
