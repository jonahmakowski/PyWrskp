from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, join_room, leave_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app, cors_allowed_origins="*")

users = {}  # To store user data, key: socket_id, value: username
groups = {'Everyone': set()}  # To store groups, key: group_name, value: set of socket_ids


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('connect')
def on_connect():
    users[request.sid] = 'server'  # Server's default username is 'server'
    emit('user_connected', {'username': 'server'}, broadcast=True)


@socketio.on('disconnect')
def on_disconnect():
    username = users[request.sid]
    del users[request.sid]
    emit('user_disconnected', {'username': username}, broadcast=True)


@socketio.on('set_username')
def set_username(data):
    username = data['username']
    if username not in users.values():
        users[request.sid] = username
        emit('username_set', {'username': username})
        emit('user_list', {'users': list(users.values())}, broadcast=True)
        emit('group_list', {'groups': list(groups.keys())}, broadcast=True)


@socketio.on('create_group')
def create_group(data):
    group_name = data['group_name']
    if group_name not in groups:
        groups[group_name] = set()
        emit('group_created', {'group_name': group_name}, broadcast=True)
        emit('group_list', {'groups': list(groups.keys())}, broadcast=True)


@socketio.on('join_group')
def join_group(data):
    group_name = data['group_name']
    if group_name in groups:
        groups[group_name].add(request.sid)
        join_room(group_name)
        emit('user_joined_group', {'username': users[request.sid], 'group_name': group_name}, room=group_name)


@socketio.on('leave_group')
def leave_group(data):
    group_name = data['group_name']
    if group_name in groups and request.sid in groups[group_name]:
        groups[group_name].remove(request.sid)
        leave_room(group_name)
        emit('user_left_group', {'username': users[request.sid], 'group_name': group_name}, room=group_name)


@socketio.on('send_message')
def send_message(data):
    message = data['message']
    recipient = data.get('recipient', None)
    if recipient:  # Private message
        emit('private_message', {'sender': users[request.sid], 'message': message}, room=recipient)
    else:  # Group message
        group_name = data['group_name']
        emit('group_message', {'sender': users[request.sid], 'message': message, 'group_name': group_name},
             room=group_name)


if __name__ == '__main__':
    socketio.run(app, debug=True)
    