import feedparser
from bs4 import BeautifulSoup
from datetime import datetime as dt

GOOGLE_URL = "http://news.google.com/news?q=covid-19&hl=fr-DZ&sort=date&gl=DZ&num=100&output=rss"



def clean(html):
    '''
    Get the text from html and do some cleaning
    '''
    soup = BeautifulSoup(html,"lxml")
    text = soup.get_text()
    text = text.replace('\xa0', ' ')
    return text

def scrap(scrapurl):
    '''
    Parse the URL, and print all the details of the news
    '''
    feeds = feedparser.parse(scrapurl).entries
    for f in feeds:

        description = clean(f.get("description", ""))
        date = dt.strptime(
            f.get("published", ""), '%a, %d %b %Y %H:%M:%S %Z')
        titre = f.get("title", "")
        url = f.get("link", "")
        print(description,date, titre, url)




if __name__ == "__main__":
    scrap(GOOGLE_URL)