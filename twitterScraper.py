import tweepy
import sys
import pandas as pd
from APIkeys import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET



def twitter_scrape(topic,size):
    df = pd.DataFrame(columns=["description", "date", "title", "url", "source"])

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)
    try:
        api.verify_credentials()
        print('Authentication Successful')
    except:
        print('Error while authenticating API')
        sys.exit(1)

    news_tweets = tweepy.Cursor(api.search, q=topic).items(int(size))


    for tweet in news_tweets:
        url=f"https://twitter.com/{tweet.user.screen_name}/status/{tweet.id}"
        description=tweet.text
        date=tweet.created_at
        title=tweet.user.name
        df.loc[len(df)] = [description, date, title, url, 'twitter']

    return df



