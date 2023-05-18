import pandas as pd

df = pd.read_excel("JobTypesFinalOG.xlsx")

df = df[df["Instances"] >= 100]

df.to_excel("JobTypesFinal.xlsx", index=False)
