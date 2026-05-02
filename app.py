from flask import Flask, render_template
from flask_socketio import SocketIO
from chat_routes import register_chat_events

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

# Register chat events
register_chat_events(socketio)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)
