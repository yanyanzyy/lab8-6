from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import random

app = Flask(__name__)
socketio = SocketIO(app)

# Predefined responses for different user inputs
responses = {
    "Recommend degrees or skills for a job position": "You might consider pursuing a degree in Computer Science or Data Science.",
    "Jobs I can apply for with my qualifications": "With your qualifications, you can apply for entry-level data analyst positions.",
    "Find a job quickly after graduation": "Networking is key! Attend job fairs and connect with industry professionals.",
    "Does my school affect my employment rate?": "Yes, graduates from well-recognized schools often have higher employment rates.",
    "Industries in high demand": "Technology, healthcare, and renewable energy industries are currently in high demand."
}

@app.route('/', methods=["POST", "GET"])
def index():
    return render_template('index.html')

@socketio.on('send_message')
def handle_send_message(data):
    user_message = data['message']
    # Check if the user's message matches one of the predefined options
    response = responses.get(user_message, "I'm sorry, I don't understand that.")
    emit('receive_message', {'response': response})

if __name__ == "__main__":
    socketio.run(app, debug=True)
