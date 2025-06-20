'''from flask_cors import CORS

from flask import Flask, request, jsonify, send_from_directory

import subprocess

app = Flask(__name__)
CORS(app)
@app.route('/')
def serve_frontend():
    return send_from_directory(app.static_folder, 'index.html')


@app.route('/run', methods=['POST'])
def run_code():
    data = request.json
    code = data.get('code', '')
    input_data = data.get('input', '')

    try:
        # Save code to temp file
        with open('temp_code.py', 'w') as f:
            f.write(code)

        # Run the code with input using subprocess
        result = subprocess.run(
            ['python', 'temp_code.py'],
            input=input_data.encode(),
            capture_output=True,
            timeout=5
        )

        output = result.stdout.decode()
        errors = result.stderr.decode()

        return jsonify({'output': output, 'errors': errors})
    except subprocess.TimeoutExpired:
        return jsonify({'output': '', 'errors': 'Error: Execution timed out'})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)'''
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import subprocess

app = Flask(__name__, static_folder='static', static_url_path='')
CORS(app)

@app.route('/')
def serve_frontend():
    return send_from_directory(app.static_folder, 'Index.html')

@app.route('/run', methods=['POST'])
def run_code():
    data = request.json
    code = data.get('code', '')
    input_data = data.get('input', '')

    try:
        with open('temp_code.py', 'w') as f:
            f.write(code)

        result = subprocess.run(
            ['python', 'temp_code.py'],
            input=input_data.encode(),
            capture_output=True,
            timeout=5
        )

        output = result.stdout.decode()
        errors = result.stderr.decode()

        return jsonify({'output': output, 'errors': errors})
    except subprocess.TimeoutExpired:
        return jsonify({'output': '', 'errors': 'Error: Execution timed out'})
        
@app.errorhandler(404)
def not_found(e):
    return send_from_directory(app.static_folder, 'index.html')
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


