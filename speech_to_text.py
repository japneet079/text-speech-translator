"""Microphone and audio-file speech recognition helpers."""

import speech_recognition as sr


def speech_to_text() -> str:
    """Listen to the microphone and return the recognized text."""
    recognizer = sr.Recognizer()

    with sr.Microphone() as microphone:
        print("Listening... speak clearly, then pause.")
        recognizer.adjust_for_ambient_noise(microphone, duration=0.5)
        audio = recognizer.listen(microphone)

    try:
        text = recognizer.recognize_google(audio)
        print(f"Heard: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, could not understand the audio.")
        return ""
    except sr.RequestError as error:
        print(f"Speech recognition service error: {error}")
        return ""


def audio_to_text(audio_file) -> str:
    """Recognize speech from an uploaded audio file (used by the web app)."""
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(audio_file) as source:
            audio = recognizer.record(source)
        return recognizer.recognize_google(audio)
    except (sr.UnknownValueError, sr.RequestError, ValueError):
        return ""