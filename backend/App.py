from flask_cors import CORS

from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)
CORS(app)
@app.route("/")
def home():
    return render_template("index.html") 


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
    app.run(host="0.0.0.0", port=5000)

