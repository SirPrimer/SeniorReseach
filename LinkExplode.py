import pandas as pd

df = pd.read_csv('links.csv')

df["linkall"] = df["linkall"].str.split(",")
df = df.explode("linkall")

df = df[df["linkall"].str.contains("urgent") == False]

df.drop(df.index[0])
df.to_csv('NonUrgentLink.csv', index=False, header=None)

df = pd.read_csv('links.csv')

df["linkall"] = df["linkall"].str.split(",")
df = df.explode("linkall")

df = df[df["linkall"].str.contains("urgent") == True]

df.drop(df.index[0])
df.to_csv('UrgentLink.csv', index=False, header=None)

