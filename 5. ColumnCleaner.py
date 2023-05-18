import os
import pandas as pd


root_directory = './test'


for directory, subdirectories, files in os.walk(root_directory):

    for subdirectory in subdirectories:

        file_path = os.path.join(directory, subdirectory, 'AllJob.xlsx')

        data = pd.read_excel(file_path)

        data = data[['jobTitle', 'jobLocation', 'jobWorkHours', 'jobWorkPattern', 'qualiAge', 'qualiEduLevel', 'qualiExperience', 'qualiGender', 'qualifications2', 'responsibilities', 'jobSalary']]

        data = data[['jobTitle', 'jobLocation', 'jobWorkHours', 'jobWorkPattern', 'qualiAge', 'qualiEduLevel', 'qualiExperience', 'qualiGender', 'qualifications2', 'responsibilities', 'jobSalary']]

        new_file_path = os.path.join(directory, subdirectory, 'AllJobClean.xlsx')

        data.to_excel(new_file_path, index=False)
