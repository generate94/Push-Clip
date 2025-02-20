import os
from flask import Flask, request, send_from_directory, jsonify
import pyperclip
from flask_cors import CORS
import socket

app = Flask(__name__)
CORS(app)

@app.after_request
def add_no_cache_headers(response):
    response.cache_control.no_cache = True
    response.cache_control.no_store = True
    response.cache_control.must_revalidate = True
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

# Dynamically get the local IP
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        s.connect(('10.254.254.254', 1))  # Doesn't need to be reachable
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

@app.route('/')
def serve_index():
    return send_from_directory(os.path.dirname(os.path.abspath(__file__)), 'index.html')

@app.route('/get_ip')
def get_ip():
    # Return the local IP as a JSON response
    return jsonify({"ip": get_local_ip()})

@app.route('/get_clipboard')
def get_clipboard():
    clipboard_content = pyperclip.paste()
    return jsonify({'clipboard': clipboard_content})

@app.route('/update_clipboard', methods=['POST'])
def update_clipboard():
    # Get data from form data
    data = request.form.get('new_clipboard')
    
    if data:
        pyperclip.copy(data)
        return jsonify({'status': 'success'})
    else:
        return jsonify({'status': 'error', 'message': 'No clipboard content provided'}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
