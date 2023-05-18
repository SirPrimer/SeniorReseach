import os
import pandas as pd

def check_word_in_responsibilities(row, word):
    resp = row['JobDescription']
    if pd.isna(resp):
        return 0
    return 1 if word in str(resp).lower() else 0

directory = './test'

for root, dirs, files in os.walk(directory):
    for file in files:
        if file == 'NewClean.xlsx':
            r_path = os.path.join(root, file)
            j_path = os.path.join(root, 'EDAVec.xlsx')

            all_jobs = pd.read_excel(j_path)
            responsibilities = pd.read_excel(r_path)

            all_jobs = all_jobs[['jobTitle', 'averageJobSalary', 'JobDescription']]

            header = [word for word in responsibilities['word'][:500] if pd.notna(word)]
            all_jobs = pd.concat([all_jobs, pd.DataFrame(columns=header)], axis=1)

            for col in header:
                all_jobs[col] = all_jobs.apply(check_word_in_responsibilities, axis=1, args=(col,))

            all_jobs = all_jobs.drop(columns=['JobDescription'])

            all_jobs.to_excel(os.path.join(root, 'NewDummyReadyLasso.xlsx'), index=False)
