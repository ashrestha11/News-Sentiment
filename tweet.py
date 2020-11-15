from tweepy import OAuthHandler
from tweepy import StreamListener
from tweepy import Stream
from tweepy import API
import keys
import json

import socketio
from flask import Flask

app = Flask(__name__)
app.debug = True


# import api keys
api_key, api_secret_key, access_token, access_token_s = keys.api_keys()


def user_tweets(status):
    if hasattr(status, 'retweeted_status'):
        return False

    elif status.in_reply_to_status_id is not None:
        return False

    elif status.in_reply_to_screen_name is not None:
        return False

    elif status.in_reply_to_user_id is not None:
        return False
    else:
        return True


class MyStreamListener(StreamListener):

    def on_status(self, status):

        # if it is the actual tweet
        if user_tweets(status):

            print(status.name)
            print(status.created_at)
            print(status.text)

            print("---------------")


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

