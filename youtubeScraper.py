
from random import sample
from APIkeys import YOUTUBE_API_KEY
import pandas as pd
import requests
SUBJECT="covid"

MAX_RESULTS=20


def youtube_scrape(topic,size):
    df = pd.DataFrame(columns=["description", "date", "title", "url", "source"])
    youtube_api_response = requests.get(
        f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={topic}&key={YOUTUBE_API_KEY}&type=video&maxResults={size}"
    )


    for item in sample(youtube_api_response.json()['items'], len(youtube_api_response.json()['items'])):
        url=f"https://www.youtube.com/embed/{item.get('id').get('videoId')}"
        title=item.get("snippet").get("title")
        description=item.get("snippet").get("description")
        date=item.get("snippet").get("publishedAt")
        df.loc[len(df)] = [description, date, title, url, 'youtube']

    return df


