
topic="covid"
size="30"


if __name__ == "__main__":
    print("scrapping from youtube")
    youtube_scrape(topic,size)
    print("scrapping from twitter")
    twitter_scrape(topic,size)
    print("scrapping from google")
    google_scrape(topic, size)