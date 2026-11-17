# Text & Speech Translator

A Python project that translates text and speech between languages using NLP — supporting both a command-line interface and a Streamlit web app.

## Features
- **Text-to-text** translation between multiple languages
- **Speech-to-speech** translation (speak → hear the translation)
- Automatic **source language detection**
- Works via **CLI** or a **browser-based web app** (with live mic recording)

## Tech Stack
- Python 3.12
- [`googletrans`](https://pypi.org/project/googletrans/) — translation
- [`langdetect`](https://pypi.org/project/langdetect/) — language detection
- [`SpeechRecognition`](https://pypi.org/project/SpeechRecognition/) — speech-to-text
- [`gTTS`](https://pypi.org/project/gTTS/) — text-to-speech
- [`pygame`](https://pypi.org/project/pygame/) — audio playback
- [`Streamlit`](https://streamlit.io/) — web UI

## Project Structure
```
Project_NLP/
├── translator.py            # language detection + translation
├── speech_to_text.py        # speech → text (mic + audio input)
├── text_to_speech.py        # text → speech (MP3 + playback)
├── main.py                  # CLI entry point
├── app.py                   # Streamlit web app
└── requirements.txt         # dependencies
```

## Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # macOS/Linux
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   For the CLI's local microphone input and audio playback, install the desktop extras too:
   ```bash
   pip install -r requirements-desktop.txt
   ```

## Usage

**CLI version:**
```bash
python main.py
```

**Web app version:**
```bash
streamlit run app.py
```

## Deploy on Streamlit Community Cloud

GitHub Pages only serves static files and cannot run this Python/Streamlit app. To publish the interactive app:

1. Sign in to [Streamlit Community Cloud](https://share.streamlit.io/) with GitHub and authorize access to this repository.
2. Select **Create app**, choose `japneet079/text-speech-translator` and the `main` branch, and set the main file path to `app.py`.
3. Deploy. Community Cloud installs the web dependencies from `requirements.txt`; the local microphone and audio-device packages in `requirements-desktop.txt` are not needed by the hosted app.

The app's speech recognition, translation, and speech synthesis features use external Google services and require network access. No repository secrets are needed for the current configuration. After deployment, Community Cloud provides the public app URL; future pushes to the selected branch are deployed automatically.

## How It Works
1. User provides input as typed text or spoken audio
2. The source language is automatically detected
3. Text is translated to the chosen target language
4. Output is returned as text and/or spoken audio

## Notes
- Requires an internet connection (uses Google's translation and speech recognition services)
- Best run on Python 3.12+ for full dependency compatibility

## Future Improvements
- Add an offline NLP translation model (e.g., Hugging Face MarianMT) as an alternative engine