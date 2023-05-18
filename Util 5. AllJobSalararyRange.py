import pandas as pd
import os

bins = [0, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, float("inf")]
labels = ["0-10000", "10000-20000", "20000-30000", "30000-40000", "40000-50000", "50000-60000", "60000-70000",
          "70000-80000", "80000-90000", "90000-100000", "100000+"]

for folder_name in os.listdir("./test"):
    folder_path = os.path.join("./test", folder_name)

    if os.path.isdir(folder_path):
        excel_path = os.path.join(folder_path, "AllJobClean.xlsx")
        all_job_clean_df = pd.read_excel(excel_path)

        intervals = pd.cut(all_job_clean_df["averageJobSalary"], bins=bins, labels=labels,
                           include_lowest=True).value_counts()

        intervals = intervals / len(all_job_clean_df)

        job_types_path = os.path.join(".", "JobTypes.xlsx")
        job_types_df = pd.read_excel(job_types_path, index_col=0)
        for interval, count in intervals.items():
            job_types_df.loc[folder_name, interval] = count

        job_types_df.to_excel(job_types_path)
