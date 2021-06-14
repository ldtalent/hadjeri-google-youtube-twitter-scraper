
from random import sample
from APIkeys import YOUTUBE_API_KEY

import requests
SUBJECT="covid"

MAX_RESULTS=20


def scrap_youtube_videos():
    youtube_api_response = requests.get(
        f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={SUBJECT}&key={YOUTUBE_API_KEY}&type=video&maxResults={MAX_RESULTS}"
    )
    print(youtube_api_response.json())

    for item in sample(youtube_api_response.json()['items'], len(youtube_api_response.json()['items'])):
        url=f"https://www.youtube.com/embed/{item.get('id').get('videoId')}"
        title=item.get("snippet").get("title")
        description=item.get("snippet").get("description")
        date=item.get("snippet").get("publishedAt")
        print(url,title, description, date)

if __name__ == "__main__":
    scrap_youtube_videos()