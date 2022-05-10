'''
This program will analyze and classify Republican vs. Democrat tweets.
The program will analyze Republican vs. Democratic tweets to determine
whether there exists a specific differentiation (word choice, tone, etc.).
Further, this program will be able to predict a politician’s party based on their tweets.

@RohanShah
ATCS Block F
May 10, 2022
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import nltk
import nltk as nlp
import re

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


data = pd.read_csv("../Data/ExtractedTweets.csv")
dataV2 = pd.concat([data.Party, data.Tweet], axis=1)
dataV2 = dataV2.head(50)
dataV2.dropna(axis = 0, inplace = True)

dataV2.Party = [1 if each == "Democrat" else 0 for each in dataV2.Party]

tweets = []
for eachTw in dataV2.Tweet:
    eachTw = re.sub("[^a-zA-Z]"," ",eachTw)
    eachTw = eachTw.lower()
    eachTw = nltk.word_tokenize(eachTw)
    #source
    eachTw = [ word for word in eachTw if not word in set(stopwords.words("english"))]
    lemma = nlp.WordNetLemmatizer()
    eachTw = [lemma.lemmatize(word) for word in eachTw]
    eachTw = " ".join(eachTw)
    tweets.append(eachTw)

print(dataV2.Party)




'''
word2count = {}
for dates in data:
    words = nltk.word_tokenize(dates)
    for word in words:
        if word not in word2count.keys():
            word2count[word] = 1
        else:
            word2count[word] += 1
'''


