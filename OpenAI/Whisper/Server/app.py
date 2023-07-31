from flask import Flask, request, jsonify
import whisper
from tempfile import NamedTemporaryFile

app = Flask(__name__)
model = whisper.load_model("base")

@app.route('/upload', methods=['POST'])
def handle_wav_upload():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    temp = NamedTemporaryFile()
    handle = request.files['file']
    handle.save(temp)
    result = model.transcribe(temp.name)

    return jsonify({'results': result['text']}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5566)
