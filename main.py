from googleScraper import google_scrape
from youtubeScraper import youtube_scrape
from twitterScraper import twitter_scrape
import pandas as pd

topic="covid"
size="30"


if __name__ == "__main__":
    print("scrapping from youtube")
    df_youtube=youtube_scrape(topic,size)
    print("scrapping from google")
    df_google=google_scrape(topic, size)
    print(df_google)
    print("scrapping from twitter")
    df_twitter=twitter_scrape(topic,size)
    data=pd.concat([df_youtube,df_google,df_twitter])
    data.to_csv('./scrapeddata.csv')
