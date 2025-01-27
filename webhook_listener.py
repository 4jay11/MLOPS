from flask import Flask, request
import subprocess
import os

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    if data and 'ref' in data and data['ref'] == 'refs/heads/main':
        # Pull latest changes
        subprocess.run(["git", "pull"], cwd="C:\\path\\to\\your\\project", shell=True)
        
        # Rebuild Flask Docker container
        subprocess.run(["docker", "build", "-t", "flask-app", "."], cwd="C:\\path\\to\\your\\project\\flask_app", shell=True)
        subprocess.run(["docker", "stop", "flask-container"], shell=True)
        subprocess.run(["docker", "run", "-d", "--rm", "--name", "flask-container", "-p", "5001:5001", "flask-app"], shell=True)

        # Rebuild Streamlit Docker container
        subprocess.run(["docker", "build", "-t", "streamlit-app", "."], cwd="C:\\path\\to\\your\\project\\streamlit_app", shell=True)
        subprocess.run(["docker", "stop", "streamlit-container"], shell=True)
        subprocess.run(["docker", "run", "-d", "--rm", "--name", "streamlit-container", "-p", "8501:8501", "streamlit-app"], shell=True)

        return "Webhook received and Docker containers restarted.", 200
    return "Invalid webhook payload.", 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
