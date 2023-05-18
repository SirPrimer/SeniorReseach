import os
import pandas as pd
import re

root_directory = './test'

for directory, subdirectories, files in os.walk(root_directory):
    for subdirectory in subdirectories:
        file_path = os.path.join(directory, subdirectory, 'EDAGender.xlsx')
        data = pd.read_excel(file_path)
        data['jobLocation'] = data['jobLocation'].apply(lambda x: re.sub(r'\([^()]*\)', '', x))
        data['province'] = data['jobLocation'].str.split(',').str[0].str.strip()
        province_dummies = pd.get_dummies(data['province'], prefix='province', dtype=int)
        data = pd.concat([data, province_dummies], axis=1)
        data = data.drop(['jobLocation', 'province'], axis=1)
        data.to_excel(os.path.join(directory, subdirectory, 'EDALocation.xlsx'), index=False)
