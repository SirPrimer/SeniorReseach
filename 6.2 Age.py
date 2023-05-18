import os
import pandas as pd
import re


root_directory = './test'


for directory, subdirectories, files in os.walk(root_directory):

    for subdirectory in subdirectories:

        file_path = os.path.join(directory, subdirectory, 'AllJobCleanEDA.xlsx')
        data = pd.read_excel(file_path)
        data['MinAge'] = ''
        data['MaxAge'] = ''
        for i in range(len(data)):
            age = str(data.at[i, 'qualiAge'])
            match = re.search(r'(\d+)\s*-\s*(\d+)', age)
            if match:
                min_age, max_age = match.group(1, 2)
                data.at[i, 'MinAge'] = min_age
                data.at[i, 'MaxAge'] = max_age
            elif 'ปีขึ้นไป' in age:
                min_age = re.search(r'(\d+)', age).group(1)
                data.at[i, 'MinAge'] = min_age
                data.at[i, 'MaxAge'] = 60
            elif re.search(r'\d+', age):
                data.at[i, 'MinAge'] = re.search(r'\d+', age).group(0)
                data.at[i, 'MaxAge'] = 60
            else:
                data.at[i, 'MinAge'] = 18
                data.at[i, 'MaxAge'] = 60
        data = data.drop(['qualiAge'], axis=1)
        data.to_excel(os.path.join(directory, subdirectory, 'EDAAge.xlsx'), index=False)
