from tweepy import OAuthHandler
from tweepy import StreamListener
from tweepy import Stream
from tweepy import API
import keys
import json

# import api keys
api_key, api_secret_key, access_token, access_token_s = keys.api_keys()


def analyze_status(text):

    if '@' not in text[0] or 'RT' not in text[0:2]:
        print(text)
    else:
        pass


class MyStreamListener(StreamListener):

    def on_data(self, raw_data):
        # load the json and filter it
        pass

    def on_status(self, status):

        try:
            print(analyze_status(status.text))

        except AttributeError:
            print(analyze_status(status.text))


class TweepyStream():

    def __init__(self, auth, listener):
        self.stream = Stream(auth=auth, listener=listener)

    def start(self, tweet_id):
        self.stream.filter(follow=tweet_id)


if __name__ == '__main__':

    myStreamListener = MyStreamListener()

    auth = OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_token_s)
    api = API(auth, wait_on_rate_limit=True,
              wait_on_rate_limit_notify=True)

    stream = TweepyStream(auth=api.auth, listener=myStreamListener)
    stream.start(['2704294333', '624413', '15110357','988955288'])

