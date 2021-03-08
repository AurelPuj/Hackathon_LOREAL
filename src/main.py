import pandas as pd
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from spacy import displacy
from sklearn.model_selection import train_test_split
from emoji_process import emoji_process
from nltk.tokenize import word_tokenize


# Load Data
train_set = pd.read_csv('../data/hackathon_loreal_train_set.csv')
test_set = pd.read_csv('../data/hackathon_loreal_train_set.csv')

nlp = spacy.load("en_core_web_sm")
all_stopwords = nlp.Defaults.stop_words


# function to lemmatize text
def lemmatization(texts):
    output = []
    for i, text in enumerate(texts):

        print(str(round(100 * i / len(texts)))+"%")
        s = [token.lemma_ for token in nlp(text)]
        output.append(' '.join(s))

    return output


def filterstopwords(texts):
    output = []
    for i, text in enumerate(texts):
        print(str(round(100 * i / len(texts))) + "%")
        text_tokens = word_tokenize(text)
        tokens_without_sw = [word for word in text_tokens if not word in all_stopwords]
        output.append(' '.join(tokens_without_sw))
    return output


def traitement(data):

    data.text = emoji_process(data.text)

    punctuation = '!"#$%&()*+-/:;<=>?@[\\]^_`{|}~,.'

    print("PONCTUATION\n")
    data['text'] = data['text'].apply(lambda x: ''.join(ch for ch in x if ch not in set(punctuation)))

    print("LOWER\n")
    # convert text to lowercase
    data['text'] = data['text'].str.lower()

    print("NUMBER\n")
    # remove numbers
    data['text'] = data['text'].str.replace("[0-9]", " ")

    print("WHITESPACE\n")
    # remove whitespaces
    data['text'] = data['text'].apply(lambda x: ' '.join(x.split()))

    print("STOPWORDS\n")
    data['text'] = filterstopwords(data['text'])

    print("LEMATIZATION\n")
    data['text'] = lemmatization(data['text'])
    data.to_csv("../data/data_process.csv", sep=";", index=False)


traitement(train_set)
