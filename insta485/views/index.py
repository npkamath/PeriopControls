"""
Insta485 index (main) view.

URLs include:
/
"""
import flask
import insta485
from flask_socketio import SocketIO
import datetime

app2 = flask.Flask(__name__)
socketio = SocketIO(app2)

@insta485.app.route('/')
def show_index():
    """Display / route."""
    context = {}
    return flask.render_template("index.html", **context)

@socketio.on('connect')
def handle_connect():
    # Emit the current time to the connected client
    socketio.emit('update_time', {'time': str(datetime.datetime.now())})

if __name__ == '__main__':
    socketio.run(app2)