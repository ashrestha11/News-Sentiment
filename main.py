"""
extract the news >> perform sentiment analysis >> transfer to database >> dashboard

"""

from pprint import pprint
from finnews.client import News
import os
import csv


class extract_news(object):

    def __init__(self):
        self.news_client = News()
        self.cnbc_news_client = self.news_client.cnbc
        self.market_watch_client = self.news_client.market_Watch
        self.wsj_client = self.news_client.wsj
        self.nasdaq_client = self.news_client.nasdaq

    def news_feed(self):

        feeds = []
        cbnc_top_news = self.cnbc_news_client.news_feed(topic='top_news')
        mw_news = self.market_watch_client.all_feeds()

        wsj_news = self.wsj_client.market_news()
        nasdaq_news = self.nasdaq_client.nasdaq_news_feed()

        news_list = [cbnc_top_news, mw_news, wsj_news, nasdaq_news]


    def to_csv(sample):

        data_path = os.path.join(os.getcwd(), 'data')
        # if it doesnt exist
        while not os.path.exists(data_path):
            # create a path
            os.mkdir(data_path)

        file_path = os.path.join(data_path, 'data.csv')

        with open(file_path,'w',encoding='UTF-8',newline=" ") as file:
            headers=['Time', 'Source', 'Title', 'Description', 'Sector']
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()

            for i in sample:
                writer.writerow(i)


if __name__ == '__main__':
    news = extract_news()
    news.news_feed()