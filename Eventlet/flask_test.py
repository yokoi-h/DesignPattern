__author__ = 'yokoi-h'

from flask import Flask

import eventlet
from eventlet import wsgi

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return 'Hi, how are you?'

if __name__ == "__main__":
    server_sock = eventlet.listen(('localhost',8080))
    wsgi.server(server_sock, app)