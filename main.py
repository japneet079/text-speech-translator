"""CLI entry point for the NLP Text & Speech Translator."""

from translator import detect_language, translate_text
from speech_to_text import speech_to_text
from text_to_speech import text_to_speech


def run():
    print("=== NLP Text & Speech Translator ===\n")

    mode = input("Choose input mode - (1) Text  (2) Speech: ").strip()
    target_lang = input("Enter target language code (e.g. hi, fr, es, ja): ").strip().lower()

    if mode == "1":
        text = input("Enter text to translate: ").strip()
    elif mode == "2":
        text = speech_to_text()
        if not text:
            print("No speech was detected. Exiting.")
            return
    else:
        print("Invalid choice. Exiting.")
        return

    if not text:
        print("No text to translate. Exiting.")
        return

    source_lang = detect_language(text)
    print(f"\nDetected source language: {source_lang}")

    translated = translate_text(text, target_lang=target_lang, source_lang=source_lang)
    print(f"Translated text: {translated}\n")

    output_mode = input("Choose output mode - (1) Text only  (2) Speech: ").strip()
    if output_mode == "2":
        print("Playing translated audio...")
        text_to_speech(translated, language=target_lang)
    else:
        print("Done.")


if __name__ == "__main__":
    run()