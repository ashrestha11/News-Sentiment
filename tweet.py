from tweepy import OAuthHandler
from tweepy import StreamListener
from tweepy import Stream
from tweepy import API
import keys
import json

# import api keys
api_key, api_secret_key, access_token, access_token_s = keys.api_keys()

# Oauth
auth = OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_s)
api = API(auth, wait_on_rate_limit=True,
          wait_on_rate_limit_notify=True)


def analyze_status(text):

    if '@' not in text[0]:
        print(text)
    else:
        pass


class MyStreamListener(StreamListener):

    def on_status(self, status):

        if not hasattr(status, "retweeted_status"):
            try:
                print(analyze_status(status.extended_tweet["full_text"]))

            except AttributeError:
                print(status.text)


myStreamListener = MyStreamListener()
myStream = Stream(auth=api.auth, listener=myStreamListener)

myStream.filter(follow=['2704294333', '624413', '15110357'])
