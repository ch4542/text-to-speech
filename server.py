from flask import Flask, request, jsonify
from vosk import Model, KaldiRecognizer
import os
import wave
import subprocess
import tempfile
import json

MODEL_PATH = os.environ.get('VOSK_MODEL_PATH', 'model')

if not os.path.isdir(MODEL_PATH):
    raise RuntimeError(f"Model not found in '{MODEL_PATH}'. Download a Vosk model and set VOSK_MODEL_PATH")

model = Model(MODEL_PATH)
app = Flask(__name__)

@app.route('/transcribe', methods=['POST'])
def transcribe():
    if 'file' not in request.files:
        return jsonify({'error': 'no file uploaded'}), 400
    uploaded = request.files['file']
    with tempfile.TemporaryDirectory() as tmpdir:
        input_path = os.path.join(tmpdir, uploaded.filename)
        uploaded.save(input_path)
        wav_path = os.path.join(tmpdir, 'audio.wav')
        # convert to 16k mono wav using ffmpeg
        cmd = ['ffmpeg', '-y', '-i', input_path, '-ar', '16000', '-ac', '1', wav_path]
        subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        wf = wave.open(wav_path, 'rb')
        rec = KaldiRecognizer(model, wf.getframerate())
        transcript = ''
        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                res = json.loads(rec.Result())
                transcript += res.get('text', '') + ' '
        final = json.loads(rec.FinalResult())
        transcript += final.get('text', '')
    return jsonify({'text': transcript.strip()})

if __name__ == '__main__':
    app.run(debug=True)
