from dataprocess import process
import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import json

# Load Data
train_set = pd.read_csv('data/hackathon_loreal_train_set.csv')
test_set = pd.read_csv('data/hackathon_loreal_test_set.csv')

if os.path.isfile('data/data_process.csv'):
    train_set = pd.read_csv('data/data_process.csv', sep=";")
else:
    process(train_set,"train_process")

X_train = train_set.text
y_train = train_set[['skincare', 'hair', 'make-up', 'other']]
categories = ['skincare', 'hair', 'make-up', 'other']
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

# Define a pipeline combining a text feature extractor with multi lable classifier
LogReg_pipeline = Pipeline([
                ('tfidf', TfidfVectorizer()),
                ('clf', OneVsRestClassifier(LogisticRegression(solver='sag'), n_jobs=1)),
            ])


if os.path.isfile('data/data_process.csv'):
    test_set = pd.read_csv('data/test_process.csv', sep=";")
else:
    process(test_set, "test_process")

X_test = test_set.text
predictions_cat = []

for category in categories:
    print('... Processing {}'.format(category))
    # train the model using X_dtm & y
    LogReg_pipeline.fit(X_train, y_train[category])
    ('clf', OneVsRestClassifier(LogisticRegression(solver='sag'), n_jobs=1)),
    # compute the testing accuracy
    prediction = LogReg_pipeline.predict(X_test)
    for i, p in enumerate(prediction):
        if len(predictions_cat) == i:
            predictions_cat.append([])
            predictions_cat[i] = [int(p)]
        else:
            if category != 'other':
                predictions_cat[i].append(int(p))
            else:
                if p == 0:
                    predictions_cat[i].append(int(p))
                else:
                    predictions_cat[i] = [0, 0, 0, 1]
print(test_set['index'].tolist())


dict = {"hash":"be432aa27d928f60", "data":{"index":test_set['index'].tolist(), "label":predictions_cat}}

with open('data.txt', 'w') as outfile:
    json.dump(dict, outfile)