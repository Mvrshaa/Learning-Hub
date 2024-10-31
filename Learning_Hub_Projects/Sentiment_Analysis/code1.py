#count the number of tweets in the given dataset
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

num_tweets = len(tweets)
print("Number of tweets:", num_tweets)

# Define the lists of happy and sad words
happy_words = ['happy', 'excited', 'great', 'nice', 'awesome', 'amazing', 'love', 'fun', 'enjoy', 'good']
sad_words = ['sad', 'depressed', 'unhappy', 'disappointed', 'miserable', 'heartbroken', 'upset', 'gloomy', 'pain', 'sorrow']

# Example tweet
tweet = "I'm really excited to learn Python with @JovianML #zerotopandas"

# Check if the tweet contains any happy or sad words
is_happy = any(word in tweet for word in happy_words)
is_sad = any(word in tweet for word in sad_words)

# Classify the tweet based on the presence of happy or sad words
if is_happy:
    print("The tweet is happy.")
elif is_sad:
    print("The tweet is sad.")
else:
    print("The sentiment of the tweet cannot be determined.")


# Count the number of happy tweets
num_happy_tweets = 0
for i in happy_words:
  for j in tweets:
    if i in j:
      num_happy_tweets+=1

print("Number of happy tweets:", num_happy_tweets)

# Calculate the percentage of happy tweets
percentage_happy_tweets = (num_happy_tweets / len(tweets)) * 100

print("Percentage of happy tweets:", percentage_happy_tweets)

# the number of tweets in the dataset that are sad
sad_words = ['sad', 'depressed', 'unhappy', 'terrible', 'horrible', 'awful', 'painful', 'bad', 'angry']

# Count the number of sad tweets
num_sad_tweets = 0
for tweet in tweets:
    if any(word in tweet for word in sad_words):
        num_sad_tweets += 1

print("Number of sad tweets:", num_sad_tweets)

# Calculate the percentage of sad tweets
percentage_sad_tweets = (num_sad_tweets / len(tweets)) * 100

print("Percentage of sad tweets:", percentage_sad_tweets)

# Count the number of happy and sad tweets
num_happy_tweets = 0
num_sad_tweets = 0
for tweet in tweets:
    if any(word in tweet for word in happy_words):
        num_happy_tweets += 1
    if any(word in tweet for word in sad_words):
        num_sad_tweets += 1

# Calculate the percentage of happy and sad tweets
percentage_happy_tweets = (num_happy_tweets / len(tweets)) * 100
percentage_sad_tweets = (num_sad_tweets / len(tweets)) * 100

# Calculate the sentiment score(the difference between the % of happy tweets and the % of sad tweets
sentiment_score = percentage_happy_tweets - percentage_sad_tweets

print("Sentiment score:", sentiment_score)







