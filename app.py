from flask import Flask, render_template, request, jsonify
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encode', methods=['POST'])
def encode():
    input_text = request.json['input_text']
    encoded_str = base64.b64encode(input_text.encode("utf-8")).decode("utf-8")
    return jsonify({'encoded_str': encoded_str})

@app.route('/decode', methods=['POST'])
def decode():
    encoded_str = request.json['encoded_str']
    try:
        decoded_str = base64.b64decode(encoded_str.encode("utf-8")).decode("utf-8")
        return jsonify({'decoded_str': decoded_str})
    except base64.binascii.Error:
        return jsonify({'error': 'Invalid base64 input'})
    except UnicodeDecodeError:
        return jsonify({'error': 'Decoding error - not a valid UTF-8 string'})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)