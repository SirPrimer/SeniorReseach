import pandas as pd
import os


root_directory = './test'


job_types_df = pd.read_excel('JobTypes.xlsx')


avg_salaries = []
instances = []


for index, row in job_types_df.iterrows():
    subfolder_name = row['JobTypes']

    all_job_clean_file = os.path.join(root_directory, subfolder_name, 'EDAFinal.xlsx')

    all_job_clean_df = pd.read_excel(all_job_clean_file)

    avg_salary = round(all_job_clean_df['averageJobSalary'].mean())
    num_instances = len(all_job_clean_df['averageJobSalary'])

    avg_salaries.append(avg_salary)
    instances.append(num_instances)

job_types_df['AverageSalary'] = avg_salaries
job_types_df['Instances'] = instances

job_types_df.to_excel('JobTypes.xlsx', index=False)
