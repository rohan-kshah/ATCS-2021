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

data = pd.read_csv("../Data/ExtractedTweets.csv")
dataV2 = pd.concat([data.Party, data.Tweet], axis=1)
dataV2.dropna(axis = 0, inplace = True)

dataV2["Party"].replace(["Democrat", "Republican"], [1, 0], inplace=True)

from nltk.corpus import stopwords

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

from sklearn.feature_extraction.text import CountVectorizer

max_features = 5000
count_vectorizer = CountVectorizer(max_features=max_features , stop_words= "english")
sparce_matrix = count_vectorizer.fit_transform(tweets).toarray()
y = dataV2.iloc[:,0].values
x = sparce_matrix
print(x)

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix

scaler = StandardScaler().fit(x)
x = scaler.transform(x)

# Split into train and test data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

'''Create Model'''
model = LogisticRegression().fit(x_train, y_train)

# Print model info
coef = model.coef_[0]

y_pred = model.predict(x_test)
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print()

print("Accuracy", model.score(x_test, y_test))

x_pred = ["Representatives of the Women’s Mining Coalition visited my office today! We discussed mining issues"]
x_pred = scaler.transform(x_pred)

# make and print prediction
if model.predict(x_pred)[0] == 1:
    print("This customer will buy an SUV.")
else:
    print("This customer will not buy an SUV.")





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


