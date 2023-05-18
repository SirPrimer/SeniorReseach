import os
import pandas as pd


root_directory = './test'


for directory, subdirectories, files in os.walk(root_directory):
    for subdirectory in subdirectories:
        file_path = os.path.join(directory, subdirectory, 'EDAAge.xlsx')
        data = pd.read_excel(file_path)
        gender_values = ['ชาย', 'หญิง', 'ไม่ระบุ']
        gender_columns = ['Gender_Male', 'Gender_Female', 'Gender_Any']
        for i, value in enumerate(gender_values):
            data[gender_columns[i]] = 0
        for i in range(len(data)):
            gender = str(data.at[i, 'qualiGender'])
            for j, value in enumerate(gender.split(',')):
                value = value.strip()
                if value in gender_values:
                    data.at[i, gender_columns[gender_values.index(value)]] = 1
        data = data.drop(['qualiGender'], axis=1)
        data.to_excel(os.path.join(directory, subdirectory, 'EDAGender.xlsx'), index=False)

