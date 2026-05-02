from flask import Flask, render_template, request, redirect
from flask_socketio import SocketIO
from chat_routes import register_chat_events
from models import save_user  # you’ll create this in models.py
from models import save_user, find_user

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = find_user(username, password)
        if user:
            return redirect('/chat')
        else:
            return "Invalid credentials", 401
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        save_user(username, password)  # insert into MongoDB
        return redirect('/login')
    return render_template('register.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

# Register chat events
register_chat_events(socketio)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)

