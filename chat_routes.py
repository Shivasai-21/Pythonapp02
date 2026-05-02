from flask_socketio import emit, join_room, leave_room

def register_chat_events(socketio):
    @socketio.on('connect')
    def handle_connect():
        emit('message', {'data': 'Welcome to Realtime Chat!'})

    @socketio.on('join')
    def handle_join(data):
        room = data['room']
        join_room(room)
        emit('message', {'data': f"Joined room {room}"}, room=room)

    @socketio.on('chat')
    def handle_chat(data):
        room = data['room']
        msg = data['msg']
        emit('chat', {'msg': msg}, room=room)

    @socketio.on('leave')
    def handle_leave(data):
        room = data['room']
        leave_room(room)
        emit('message', {'data': f"Left room {room}"}, room=room)
