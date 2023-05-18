import os
import pandas as pd

root_directory = './test'

try:
    subdirectory_names = next(os.walk(root_directory))[1]
except StopIteration:
    subdirectory_names = []

df = pd.DataFrame({'JobTypes': subdirectory_names})

output_file_path = 'JobTypes.xlsx'

df.to_excel(output_file_path, index=False)
