import socketio
from flask import Flask
import threading
import tweet


app = Flask(__name__)
app.debug = True


@app.route("/")
def hello():
    return tweet.main()


if __name__ == '__main__':
    app.run(debug=True)
