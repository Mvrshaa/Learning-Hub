import nltk
#processing textual data
from textblob import TextBlob
#classifier that can be used for binary classification tasks
from sklearn.linear_model import LogisticRegression
#converts a collection of text documents into a matrix of token counts
from sklearn.feature_extraction.text import CountVectorizer
# evaluate the accuracy of a classification model
from sklearn.metrics import accuracy_score

nltk.download('punkt')

# define a function to get the sentiment of a tweet
def get_tweet_sentiment(tweet):
    # create TextBlob object of the tweet text
    analysis = TextBlob(tweet)
    
    # return sentiment analysis
    if analysis.sentiment.polarity > 0:
        return 'happy'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'sad'

# define a list of tweets
tweets = [
    "Wow, what a great day today!! #sunshine",
    "I feel sad about the things going on around us. #covid19",
    "I'm really excited to learn Python with @JovianML #zerotopandas",
    "This is a really nice song. #linkinpark",
    "The python programming language is useful for data science",
    "Why do bad things happen to me?",
    "Apple announces the release of the new iPhone 12. Fans are excited.",
    "Spent my day with family!! #happy",
    "Check out my blog post on common string operations in Python. #zerotopandas",
    "Freecodecamp has great coding tutorials. #skillup"
]

# initialize counters for happy and sad tweets
happy_tweets = 0
sad_tweets = 0

# loop through each tweet and count the happy and sad ones
for tweet in tweets:
    sentiment = get_tweet_sentiment(tweet)
    if sentiment == 'happy':
        happy_tweets += 1
    elif sentiment == 'sad':
        sad_tweets += 1

# calculate percentages
total_tweets = len(tweets)
happy_percent = (happy_tweets / total_tweets) * 100
sad_percent = (sad_tweets / total_tweets) * 100

# calculate sentiment score
sentiment_score = happy_percent - sad_percent


# create a list of labels for the tweets
labels = [get_tweet_sentiment(tweet) for tweet in tweets]

# create a CountVectorizer object to convert text into numerical features
vectorizer = CountVectorizer()

# convert the list of tweets into a matrix of numerical features
X = vectorizer.fit_transform(tweets)

# create a logistic regression model
model = LogisticRegression()

# train the model on the matrix of features and the list of labels
model.fit(X, labels)

# use the model to predict the sentiment of the tweets
predictions = model.predict(X)

# calculate accuracy score of the model
accuracy = accuracy_score(labels, predictions)
# print the results
print("Number of happy tweets:", happy_tweets)
print("Percentage of happy tweets: {:.2f}%".format(happy_percent))
print("Number of sad tweets:", sad_tweets)
print("Percentage of sad tweets: {:.2f}%".format(sad_percent))
print("Sentiment score: {:.2f}".format(sentiment_score))

# print the results
print("Accuracy of the model: {:.2f}%".format(accuracy*100))


