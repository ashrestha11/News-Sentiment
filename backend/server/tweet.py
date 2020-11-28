from tweepy import OAuthHandler
from tweepy import StreamListener
from tweepy import Stream
from tweepy import API
from flask import Flask, render_template
from flask_socketio import SocketIO
import keys
import json
from threading import Thread
from . import utils

# Flask app
app = Flask(__name__)
app.debug = True

#Socket
socketio = SocketIO(app)


# import api keys
api_key, api_secret_key, access_token, access_token_s = keys.api_keys()


## auth tweets
auth = OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_s)
api = API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


class MyStreamListener(StreamListener):

    def on_data(self, raw_data):

        data = json.loads(raw_data)
        socketio.emit('stream_channel',
                      data,
                      json=True,
                      namespace='/demo_streaming')

    def on_status(self, status):

        # if it is the actual tweet
        if utils.user_tweets(status):

            print(status.name)
            print(status.created_at)
            print(status.text)

            print("---------------")


def stream_filter(users):

    stream = Stream(auth,MyStreamListener())
    stream.filter(follow=users)


@app.route("/")
def home():
    return render_template('index.html')

if __name__ == '__main__':

    users=['2704294333', '624413', '15110357', '988955288']
    Thread(target=stream_filter, args=(users,)).start()
    # Start the server
    socketio.run(app, debug=True, host='127.0.0.1')



    #stream.start(['2704294333', '624413', '15110357', '988955288'])

