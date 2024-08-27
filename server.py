from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)


@app.route("/")
def index():
    # return "Hello from Server"
    return render_template("index.html")


@socketio.on("connect")
def test_message(message):
    print(message)
    emit("my_connect_response", {"data": "Connection to client acknowledged"})


if __name__ == "__main__":
    socketio.run(app)

"""
Pub sub
    Client subs to some topic
Elasticache/Redis
Dockerize the server
Deploy into AWS EKS env
Authenticated users
"""
