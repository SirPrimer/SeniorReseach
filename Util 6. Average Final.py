import pandas as pd
import os
import numpy as np

root_directory = './test'

job_types_df = pd.read_excel('JobTypes.xlsx')

means = {}
instances = {}

for index, row in job_types_df.iterrows():
    subfolder_name = row['JobTypes']

    all_job_clean_file = os.path.join(root_directory, subfolder_name, 'EDAFinal.xlsx')

    all_job_clean_df = pd.read_excel(all_job_clean_file)

    for column in ['qualiExperience', 'eduLevel_ต่ำกว่า', 'eduLevel_ปริญญาตรี', 'eduLevel_ปริญญาโท', 'eduLevel_ปวช.', 'eduLevel_ปวส.', 'eduLevel_ม.6', 'eduLevel_ไม่มีวุฒิการศึกษา', 'eduLevel_ไม่ระบุ', 'jobWorkPattern_งานนอกเวลา', 'jobWorkPattern_งานประจำ', 'jobWorkPattern_งานอิสระ', 'jobWorkPattern_สหกิจศึกษา', 'jobWorkPattern_สัญญาจ้าง', 'MinAge', 'MaxAge', 'Gender_Male', 'Gender_Female', 'Gender_Any', 'province_กรุงเทพมหานคร']:
        if column not in all_job_clean_df.columns:
            means.setdefault(column, []).append(0)
            instances.setdefault(column, []).append(0)
            continue
        column_mean = all_job_clean_df[column].mean()
        column_instances = len(all_job_clean_df[column])
        means.setdefault(column, []).append(column_mean)
        instances.setdefault(column, []).append(column_instances)

for column in means:
    job_types_df[f'{column}_Mean'] = means[column]

job_types_df.to_excel('JobTypesFinal.xlsx', index=False)
