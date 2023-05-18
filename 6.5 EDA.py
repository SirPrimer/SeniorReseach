import os
import pandas as pd
import re

root_directory = './test'

for directory, subdirectories, files in os.walk(root_directory):
    for subdirectory in subdirectories:
        file_path = os.path.join(directory, subdirectory, 'EDALocation.xlsx')
        data = pd.read_excel(file_path)

        data = data.drop(columns=['jobWorkHours', 'JobDescription'])

        output_file_path = os.path.join(directory, subdirectory, 'EDAFinal.xlsx')
        data.to_excel(output_file_path, index=False)
