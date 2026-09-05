"""Convert translated text to speech and play it back."""

import os
from pathlib import Path
from gtts import gTTS
import pygame

OUTPUT_FOLDER = Path(__file__).resolve().parent / "output"


def text_to_speech(text: str, language: str, play_audio: bool = True) -> str:
    """Save text as an MP3 and optionally play it. Returns the file path."""
    cleaned_text = text.strip()
    if not cleaned_text:
        raise ValueError("There is no text to convert to speech.")
    if not language:
        raise ValueError("A language code is required for speech output.")

    OUTPUT_FOLDER.mkdir(exist_ok=True)
    audio_path = OUTPUT_FOLDER / "translated_output.mp3"

    gTTS(text=cleaned_text, lang=language).save(str(audio_path))

    if play_audio:
        pygame.mixer.init()
        pygame.mixer.music.load(str(audio_path))
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    return str(audio_path)