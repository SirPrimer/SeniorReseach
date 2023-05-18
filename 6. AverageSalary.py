import os
import pandas as pd
import re


root_directory = './test'


for directory, subdirectories, files in os.walk(root_directory):

    for subdirectory in subdirectories:

        file_path = os.path.join(directory, subdirectory, 'AllJobClean.xlsx')
        data = pd.read_excel(file_path)
        data['jobSalaryLow'] = ''
        data['jobSalaryHigh'] = ''
        data['averageJobSalary'] = ''
        for i in range(len(data)):
            salary = str(data.at[i, 'jobSalary'])
            match = re.search(r'(\d[\d, ]*)\s*(?:-|to|and|or)?\s*(\d[\d, ]*)?', salary)
            if match:
                low, high = match.group(1, 2)
                low = re.sub(r'[^\d]+', '', low)
                high = re.sub(r'[^\d]+', '', high) if high else ''
                data.at[i, 'jobSalaryLow'] = low
                data.at[i, 'jobSalaryHigh'] = high
                if high:
                    data.at[i, 'averageJobSalary'] = (int(low) + int(high)) / 2
                else:
                    data.at[i, 'averageJobSalary'] = low
            else:
                data.at[i, 'jobSalaryLow'] = re.sub(r'[^\d]+', '', salary)
                data.at[i, 'jobSalaryHigh'] = ''
                data.at[i, 'averageJobSalary'] = ''
        data.to_excel(file_path, index=False)
