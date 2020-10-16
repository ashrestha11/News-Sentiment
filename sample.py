from pprint import pprint
from finnews.client import News
import os

# Create a new instance of the News Client.
news_client = News()

# Grab the CNBC News Client.
cnbc_news_client = news_client.cnbc
market_watch_client = news_client.market_Watch
wsj_client = news_client.wsj
nasdaq_client = news_client.nasdaq

# Grab the top news.
cbnc_top_news = cnbc_news_client.news_feed(topic='top_news')
mw_news = market_watch_client.top_stories()

## wsj

wsj_news = wsj_client.market_news()
nasdaq_news = nasdaq_client.nasdaq_news_feed()

# Print it.
#pprint(cbnc_top_news)
#pprint(mw_news)


for i in wsj_news:
    print(i)
    title = i['title']
    description = i['description']
    date = i['pubDate']
    type = i['articletype']


