import os
import pandas as pd

root_directory = './test'

for directory, subdirectories, files in os.walk(root_directory):

    for file in files:

        if file.endswith('AllJob.xlsx'):

            file_path = os.path.join(directory, file)

            data = pd.read_excel(file_path)

            data = data[data['jobSalary'].astype(str).str.count('\d') >= 4]

            data.to_excel(file_path, index=False)