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
import nltk
import nltk as nlp
import re

data = pd.read_csv("../Data/ExtractedTweets.csv")
dataV2 = pd.concat([data.Party, data.Tweet], axis=1)
dataV2.dropna(axis = 0, inplace = True)

dataV2["Party"].replace(["Democrat", "Republican"], [1, 0], inplace=True)

from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sentimentFinder = SentimentIntensityAnalyzer()


#create func that turns individual tweet into token and convert etc

def convertTweet(tw):
    tw = re.sub("[^a-zA-Z]"," ",tw)
    tw = tw.lower()
    tw = nltk.word_tokenize(tw)

    #source
    tw = [ word for word in tw if not word in set(stopwords.words("english"))]
    lemma = nlp.WordNetLemmatizer()
    tw = [lemma.lemmatize(word) for word in tw]
    tw = " ".join(tw)
    return tw

tweets = []
sentiments = []
for eachTw in dataV2.Tweet:
    tweetSentiment = sentimentFinder.polarity_scores(eachTw)
    sentiments.append(tweetSentiment.get('compound'))
    eachTw = convertTweet(eachTw)
    tweets.append(eachTw)

from sklearn.feature_extraction.text import CountVectorizer

max_feat = 3000
count_vectorizer = CountVectorizer(max_features=max_feat , stop_words= "english")
x_vector = count_vectorizer.fit_transform(tweets).toarray()
x = [[x_vector, sentiments]].values

y = dataV2.iloc[:,0].values

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

'''
predTweet = "Representatives of the Women’s Mining Coalition visited my office today! We discussed mining issues"
predTweet = [convertTweet(predTweet)]
max_feat2 = 9
count_vectorizer2 = CountVectorizer(max_features=max_feat2 , stop_words= "english")
x_pred = count_vectorizer2.fit_transform(predTweet).toarray()

x_pred = scaler.transform(x_pred)

# make and print prediction
if model.predict(x_pred)[0] == 1:
    print("This tweet is likely from a Democrat.")
else:
    print("This tweet is likely from a Republican.")
'''


