"""
extract the news >> perform sentiment analysis >> transfer to database >> dashboard

"""

import finnews

from pprint import pprint
from finnews.client import News

# Create a new instance of the News Client.
news_client = News()

# Grab the CNBC News Client.
cnbc_news_client = news_client.cnbc
market_watch_client = news_client.market_Watch

# Grab the top news.
cbnc_top_news = cnbc_news_client.news_feed(topic='top_news')
mw_news = market_watch_client.real_time_headlines()

# Print it.
pprint(cbnc_top_news)
pprint(mw_news)

