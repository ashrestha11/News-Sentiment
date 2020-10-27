from tweepy import OAuthHandler
from tweepy import StreamListener
from tweepy import Stream
from tweepy import API
import keys

# import api keys
api_key, api_secret_key, access_token,access_token_s = keys.api_keys()

# Oauth
auth = OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_s)
api = API(auth, wait_on_rate_limit=True,
          wait_on_rate_limit_notify=True)



class MyStreamListener(StreamListener):

    def on_status(self, status):
        print(status.text)


myStreamListener = MyStreamListener()
myStream = Stream(auth = api.auth, listener=myStreamListener)




