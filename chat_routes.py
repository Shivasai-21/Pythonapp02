from flask_socketio import emit, join_room
from models import save_message, get_messages

def register_chat_events(socketio):
    @socketio.on('join')
    def handle_join(data):
        room = data['room']
        join_room(room)
        history = get_messages(room)
        emit('history', {'messages': history}, room=request.sid)

    @socketio.on('chat')
    def handle_chat(data):
        room, user, msg = data['room'], data['user'], data['msg']
        save_message(room, user, msg)
        emit('chat', {'user': user, 'msg': msg}, room=room)
