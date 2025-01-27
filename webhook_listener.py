from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Webhook is listening", 200

@app.route('/webhook', methods=['POST'])
def webhook():
    # Pull the latest Docker image and run it
    os.system("docker pull your_docker_username/my-app:latest")
    os.system("docker run -d -p 8080:80 your_docker_username/my-app:latest")
    return "Container started", 200

if __name__ == '__main__':
    app.run(port=5000)
