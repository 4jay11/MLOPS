from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return "Webhook is listening", 200


app = Flask(__name__)

@app.route('/webhook', methods=['POST', 'GET'])
def webhook():
    try:
        # Pull the Docker image
        image_name = "ajay0411/mlops"
        pull_result = subprocess.run(['docker', 'pull', image_name], capture_output=True, text=True)
        if pull_result.returncode != 0:
            return jsonify({'error': pull_result.stderr}), 500
        
        # Run the Docker container
        container_name = 'mlops' # Default name
        port_mapping = '8501:8501'  # Default port mapping
        
        run_result = subprocess.run(
            ['docker', 'run', '-d', '--name', container_name, '-p', port_mapping, image_name],
            capture_output=True, text=True
        )
        if run_result.returncode != 0:
            return jsonify({'error': run_result.stderr}), 500
        
        return jsonify({
            'message': f'Container {container_name} running successfully!',
            'container_id': run_result.stdout.strip()
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000 ,debug=True)

