import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from pythainlp.tokenize import word_tokenize
from pythainlp.corpus import thai_stopwords
import re
import os

stop_word = list(thai_stopwords())

def cleanText(text):
    text = str(text)
    text = re.sub('[^ก-๙a-zA-Z\s]','', text)
    sentence = word_tokenize(text, engine="multi_cut")
    result = [word for word in sentence if word not in stop_word and " " not in word]
    return ",".join(result)

def tokenize(d):
    result = d.split(",")
    result = list(filter(None, result))
    return result

input_dir = './test'
output_dir = './test'

for subdir, dirs, files in os.walk(input_dir):
    for file in files:
        if file == 'EDAVec.xlsx':
            path = os.path.join(subdir, file)
            print("Processing file:", path)
            df = pd.read_excel(path)
            new_text = [cleanText(txt) for txt in df['JobDescription']]
            vectorizer = CountVectorizer(tokenizer=tokenize)
            transformed_data = vectorizer.fit_transform(new_text)
            count_data = zip(vectorizer.get_feature_names_out(), np.ravel(transformed_data.sum(axis=0)))
            keyword_df = pd.DataFrame(columns = ['word', 'count'])
            keyword_df['word'] = vectorizer.get_feature_names_out()
            keyword_df['count'] = np.ravel(transformed_data.sum(axis=0))
            keyword_df = keyword_df.sort_values(by=['count'], ascending=False)
            output_path = os.path.join(subdir, 'VecMultiToken.xlsx')
            keyword_df.to_excel(output_path, index=False)
            print("Saved VecMultiToken to:", output_path)
