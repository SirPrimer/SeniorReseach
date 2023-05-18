import os
import pandas as pd


root_directory = './test'


for directory, subdirectories, files in os.walk(root_directory):

    for subdirectory in subdirectories:

        file_path1 = os.path.join(directory, subdirectory, 'nonurgent.xlsx')

        file_path2 = os.path.join(directory, subdirectory, 'urgent.xlsx')
        if os.path.exists(file_path2):

            data1 = pd.read_excel(file_path1)
            data2 = pd.read_excel(file_path2)

            data1 = data1._append(data2)
        else:

            data1 = pd.read_excel(file_path1)

        new_file_path = os.path.join(directory, subdirectory, 'AllJob.xlsx')

        data1.to_excel(new_file_path, index=False)




