import pandas as pd
import nltk
nltk.download('punkt')
from nltk import word_tokenize

train_set = pd.read_csv('hackathon_loreal_train_set.csv')
test_set = pd.read_csv('hackathon_loreal_train_set.csv')

# Lower text
train_set = train_set.applymap(lambda text:text.lower() if type(text) == str else text)

# Tokenize
train_set = train_set.applymap(lambda text:word_tokenize(text) if type(text) == str else text)
print(train_set['text'])

