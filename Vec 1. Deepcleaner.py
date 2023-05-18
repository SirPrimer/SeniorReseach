import os
import pandas as pd
from pythainlp.corpus import thai_stopwords
from nltk.corpus import stopwords

thai_stop_words = set(thai_stopwords())
english_stop_words = set(stopwords.words('english'))

stop_words = thai_stop_words.union(english_stop_words)

root_directory = './test'

for directory, subdirectories, files in os.walk(root_directory):
    for file in files:
        if file == 'VecDeepcutToken.xlsx':
            file_path = os.path.join(directory, file)
            df = pd.read_excel(file_path)
            rows_to_remove = []
            for i, row in df.iterrows():
                word = str(row['word'])
                if word.lower() in stop_words:
                    rows_to_remove.append(i)

            df = df.drop(rows_to_remove)

            new_file_path = os.path.join(directory, 'DeepClean.xlsx')
            df.to_excel(new_file_path, index=False)
