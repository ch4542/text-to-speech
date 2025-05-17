# Text to Speech Demo

This repository contains simple Web Speech API examples for converting text to speech and speech to text. The demos rely only on client-side code.

## Overview

- **index.html** – demonstrates a combined interface for text-to-speech and speech-to-text. It loads `index-style.css` for styling and now supports voice selection and microphone recognition.
- **speech-to-text.html** – focuses solely on converting spoken audio into text and uses `speech-to-text.css`.
- **style.css** – an additional stylesheet with dark-themed styles that some pages reference.

The examples run directly in the browser for microphone input. A small Flask server is included to enable uploading audio files for transcription with the offline Vosk library.

## Opening the HTML files

1. Clone or download this repository.
2. Open `index.html` or `speech-to-text.html` directly in your web browser (e.g. by double-clicking the file or dragging it into a browser window).

## Browser requirements

These examples rely on the Web Speech API:

- `speechSynthesis` for text-to-speech.
- `SpeechRecognition` for speech-to-text.

`SpeechRecognition` is currently available only in certain browsers, such as Google Chrome. If your browser does not expose this API, the speech-to-text demo will not work.

## Known issues

- Browsers without Web Speech API support cannot run these demos.
- When opening the files directly from `file://`, microphone access may be restricted. If recognition fails to start, try serving the files with a simple HTTP server (e.g. `python -m http.server`).



## Local transcription of uploaded files

1. Install Python 3 and `ffmpeg`.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Download a Vosk model and unpack it into a folder named `model` (or set `VOSK_MODEL_PATH`). Example:
   ```bash
   wget https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip
   unzip vosk-model-small-en-us-0.15.zip -d model
   ```
4. Run the Flask server:
   ```bash
   python server.py
   ```
5. Open `index.html` or `speech-to-text.html` in your browser (preferably via `python -m http.server`). Upload audio or video files to see the transcript returned from the local server.
