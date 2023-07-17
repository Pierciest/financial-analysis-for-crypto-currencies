# FORMATTING LATER #
from modules.dates import daterange, date
from modules.loginCred import login,tweepy

Count = 5000
year = 2023
month = 6
day = 23
Date = date(year, month, day)
CoinL = "bitcoin"
CoinS = "btc"


Dates = []
for dt in daterange(Date):
    Dates.append(dt.strftime("%Y-%m-%d"))

search_termLong = CoinL + "-filter:retweets"
search_termShort = CoinS + "-filter:retweets"

api = login("login.txt")

all_tweets = []
all_users = []
all_verified = []
all_follower_count = []
all_creation_date = []
Lengths = []
Length = []
for i in Dates:
    tweets = tweepy.Cursor(api.search_tweets, q=search_termLong, lang="en", since=i, tweet_mode="extended").items(Count / 2)
    tweets2 = tweepy.Cursor(api.search_tweets, q=search_termShort, lang="en", since=i, tweet_mode="extended").items(Count / 2)
    # While writing on python make api.search, api.search_tweets
    for tweet in tweets:
        all_tweets.append(tweet.full_text)
        all_users.append(tweet.user.screen_name)
        all_verified.append(tweet.user.verified)
        all_follower_count.append(tweet.user.followers_count)
        all_creation_date.append(tweet.user.created_at)
        Length.append(tweet.full_text)

    for tweet in tweets2:
        all_tweets.append(tweet.full_text)
        all_users.append(tweet.user.screen_name)
        all_verified.append(tweet.user.verified)
        all_follower_count.append(tweet.user.followers_count)
        all_creation_date.append(tweet.user.created_at)
        Length.append(tweet.full_text)

    Lengths.append(len(Length))
    Length.clear()

print(all_tweets)
print(all_users)
print(all_verified)
print(all_follower_count)
print(all_creation_date)
print(Lengths)

