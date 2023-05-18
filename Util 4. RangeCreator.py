import pandas as pd

job_types_df = pd.read_excel("JobTypes.xlsx")

bins = [0, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, float("inf")]

labels = ["0-10000", "10000-20000", "20000-30000", "30000-40000", "40000-50000", "50000-60000",
          "60000-70000", "70000-80000", "80000-90000", "90000-100000", "100000+"]

job_types_df[labels] = pd.DataFrame([[0] * len(labels)], index=job_types_df.index)

job_types_df.to_excel("JobTypes.xlsx", index=False)
