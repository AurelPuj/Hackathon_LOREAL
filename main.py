import pandas as pd
import spacy
from spacy import displacy
from sklearn.model_selection import train_test_split

# Load Data
train_set = pd.read_csv('hackathon_loreal_train_set.csv')
test_set = pd.read_csv('hackathon_loreal_train_set.csv')

nlp = spacy.load("en_core_web_sm")


# function to lemmatize text
def lemmatization(texts):
    output = []
    for i, text in enumerate(texts):
        print(str(round(100*(i+1)/len(texts)))+"%")
        s = [token.lemma_ for token in nlp(text)]
        output.append(' '.join(s))

    return output


def traitement(data):

    punctuation = '!"#$%&()*+-/:;<=>?@[\\]^_`{|}~'

    data['text'] = data['text'].apply(lambda x: ''.join(ch for ch in x if ch not in set(punctuation)))

    # convert text to lowercase
    data['text'] = data['text'].str.lower()

    # remove numbers
    data['text'] = data['text'].str.replace("[0-9]", " ")

    # remove whitespaces
    data['text'] = data['text'].apply(lambda x: ' '.join(x.split()))

    data['text'] = lemmatization(data['text'])

    print(data['text'])

traitement(train_set)

print(train_set)
