# Text to Speech Demo

This repository contains simple Web Speech API examples for converting text to speech and speech to text.

## Overview

- **index.html** – demonstrates a combined interface for text-to-speech and speech-to-text. It loads `index-style.css` for styling.
- **speech-to-text.html** – focuses solely on converting spoken audio into text and uses `speech-to-text.css`.
- **style.css** – an additional stylesheet with dark-themed styles that some pages reference.

No server-side code is required. Simply open the HTML files in your browser.

## Opening the HTML files

1. Clone or download this repository.
2. Open `index.html` or `speech-to-text.html` directly in your web browser (e.g. by double-clicking the file or dragging it into a browser window).

## Browser requirements

These examples rely on the Web Speech API:

- `speechSynthesis` for text-to-speech.
- `SpeechRecognition` for speech-to-text.

`SpeechRecognition` is currently available only in certain browsers, such as Google Chrome. If your browser does not expose this API, the speech-to-text demo will not work.

## Known issues

- The HTML pages contain malformed markup and may not render perfectly. For example, some script tags are incomplete.
- Browsers without Web Speech API support cannot run these demos.
- When opening the files directly from `file://`, microphone access may be restricted. If recognition fails to start, try serving the files with a simple HTTP server (e.g. `python -m http.server`).


