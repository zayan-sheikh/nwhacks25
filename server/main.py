from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS

import lang

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins='*')

    
def send_state():
    while True:
        lang.prompt()  # for testing
        state = lang.getState()
        socketio.emit('state', state)
        print(f"Sent: {state}")


if __name__ == "__main__":
    socketio.start_background_task(send_state)
    socketio.run(app, host='localhost', port=6969)