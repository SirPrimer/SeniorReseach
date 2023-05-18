import os
import pandas as pd
from pythainlp.corpus import thai_stopwords
from nltk.corpus import stopwords

# Get the stop words
thai_stop_words = set(thai_stopwords())
english_stop_words = set(stopwords.words('english'))

# Combine stop words for both languages
stop_words = thai_stop_words.union(english_stop_words)

# Set the root directory to search for files
root_directory = './test'

# Loop through each directory and subdirectory in the root directory
for directory, subdirectories, files in os.walk(root_directory):
    # Loop through each file in the subdirectory
    for file in files:
        # Check if the file is the VecDeepcutToken.xlsx file
        if file == 'VecNewMMToken.xlsx':
            # Create the file path for the Excel file
            file_path = os.path.join(directory, file)
            # Read the Excel file into a DataFrame
            df = pd.read_excel(file_path)

            # Identify the rows to remove
            rows_to_remove = []
            for i, row in df.iterrows():
                word = str(row['word'])
                if word.lower() in stop_words:
                    rows_to_remove.append(i)

            # Remove the identified rows
            df = df.drop(rows_to_remove)

            # Save the cleaned DataFrame
            new_file_path = os.path.join(directory, 'NewClean.xlsx')
            df.to_excel(new_file_path, index=False)


print(stopwords.words('english'))