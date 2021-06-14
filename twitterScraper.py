import tweepy
import sys
from APIkeys import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET



def getTweets(counts=30):

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)
    try:
        api.verify_credentials()
        print('Authentication Successful')
    except:
        print('Error while authenticating API')
        sys.exit(1)

    news_tweets = tweepy.Cursor(api.search, q='covid').items(counts)
    for tweet in news_tweets:
        url=f"https://twitter.com/{tweet.user.screen_name}/status/{tweet.id}"
        description=tweet.text
        date=tweet.created_at
        title=tweet.user.name
        url=url
        print(description,date, title, url)

if __name__ == "__main__":
    getTweets()