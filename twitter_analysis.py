'''
This program will classify Republican vs. Democrat tweets.
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
import matplotlib.pyplot as plt

data = pd.read_csv("../Data/ExtractedTweets.csv")
#creating a new dataset without the twitter handles
dataV2 = pd.concat([data.Party, data.Tweet], axis=1)
dataV2.dropna(axis = 0, inplace = True)

#replacing the party description with integers in order to be able to classify
dataV2["Party"].replace(["Democrat", "Republican"], [1, 0], inplace=True)

from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sentimentFinder = SentimentIntensityAnalyzer()


#convertTweet takes an invidual tweet and reduces
# it to just lowercase important words and then converts it into a token
def convertTweet(tw):
    tw = re.sub("[^a-zA-Z]"," ",tw)
    tw = tw.lower()
    tw = nltk.word_tokenize(tw)

    #http://techflare.blog/how-to-build-sentiment-analysis-with-nltk-and-sciki-learn-in-python/
    tw = [ word for word in tw if not word in set(stopwords.words("english"))]
    lemma = nlp.WordNetLemmatizer()
    tw = [lemma.lemmatize(word) for word in tw]
    tw = " ".join(tw)
    return tw

tweets = []
sentiments = []
for eachTw in dataV2.Tweet:
    #using nltk's embedded functions to find the polarity scores of a tweet
    tweetSentiment = sentimentFinder.polarity_scores(eachTw)
    #appending the total polarity score (positive, neutral, negative combined) of a single tweet into a list
    sentiments.append(tweetSentiment.get('compound'))
    eachTw = convertTweet(eachTw)
    tweets.append(eachTw)

from sklearn.feature_extraction.text import CountVectorizer

#creating bag of words model through using CountVectorizer()
#https://gist.github.com/1fmusic/e88a3e3616a8c76cdf95b3d5521df84a
max_feat = 3000
count_vectorizer = CountVectorizer(max_features=max_feat , stop_words= "english")
x_vector = count_vectorizer.fit_transform(tweets).toarray()

x = x_vector
y = dataV2.iloc[:,0].values

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix

scaler = StandardScaler().fit(x)
x = scaler.transform(x)

#Split into train and test data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

'''Create Bag of Words Model'''
model = LogisticRegression().fit(x_train, y_train)

# Print model info
coef = model.coef_[0]

y_pred = model.predict(x_test)
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print()

print("Accuracy for model based on bag-of-words", model.score(x_test, y_test))

sentiments = np.array(sentiments)
x2 = sentiments
x2_train, x2_test, y2_train, y2_test = train_test_split(x2, y, test_size = 0.2, random_state = 42)
x2_train = x2_train.reshape(-1, 1)

'''Create Sentiment Model'''
model = LogisticRegression().fit(x2_train, y2_train)

# Print model info
coef = model.coef_[0]
x2_test = x2_test.reshape(-1, 1)
y2_pred = model.predict(x2_test)
print("Confusion Matrix:")
print(confusion_matrix(y2_test, y2_pred))
print()

print("Accuracy for model with sentiment", model.score(x2_test, y2_test))