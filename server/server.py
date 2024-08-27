from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)


@app.route("/")
def index():
    return render_template("index.html")


@socketio.on("my_event")
def test_message(message):
    emit("my_response", {"data": message["data"]})


if __name__ == "__main__":
    socketio.run(app)
