from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)  # Para comunicação em tempo real

@app.route('/')
def home():
    return render_template('index.html')  # Página inicial

# Evento para mensagens tipo WhatsApp
@socketio.on('message')
def handle_message(data):
    socketio.emit('message', data)  # Broadcast para todos os usuários

if __name__ == '__main__':
    socketio.run(app, debug=True)
