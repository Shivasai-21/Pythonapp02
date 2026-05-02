var socket = io();

socket.on('message', function(data) {
    document.getElementById('chatbox').innerHTML += "<p>" + data.data + "</p>";
});

socket.on('chat', function(data) {
    document.getElementById('chatbox').innerHTML += "<p><b>Chat:</b> " + data.msg + "</p>";
});

function joinRoom() {
    var room = document.getElementById('room').value;
    socket.emit('join', {room: room});
}

function sendMessage() {
    var room = document.getElementById('room').value;
    var msg = document.getElementById('msg').value;
    socket.emit('chat', {room: room, msg: msg});
}
