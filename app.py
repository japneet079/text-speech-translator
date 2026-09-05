"""Streamlit web UI for the NLP Text & Speech Translator."""

import streamlit as st
from translator import detect_language, translate_text
from speech_to_text import audio_to_text
from text_to_speech import text_to_speech

LANGUAGES = {
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Japanese": "ja",
    "Chinese (Simplified)": "zh-cn",
    "Russian": "ru",
    "Arabic": "ar",
}

st.set_page_config(page_title="Language Translator", page_icon="🌐")
st.title("Text & Speech Translator")

input_mode = st.radio("Choose input type:", ["Text", "Speak (mic)"])

text_input = ""

if input_mode == "Text":
    text_input = st.text_area("Enter text to translate:")
else:
    audio_value = st.audio_input("Record what you want to translate")
    if audio_value is not None:
        with st.spinner("Transcribing audio..."):
            text_input = audio_to_text(audio_value)
        if text_input:
            st.success(f"Transcribed text: {text_input}")
        else:
            st.error("Could not understand the audio. Try recording again, speaking clearly.")

target_lang_name = st.selectbox("Translate to:", list(LANGUAGES.keys()))
target_lang = LANGUAGES[target_lang_name]

output_as_audio = st.checkbox("Also generate speech output")

if st.button("Translate"):
    if not text_input.strip():
        st.warning("Please enter text or record audio first.")
    else:
        source_lang = detect_language(text_input)
        st.write(f"Detected source language: `{source_lang}`")

        with st.spinner("Translating..."):
            translated = translate_text(text_input, target_lang=target_lang, source_lang=source_lang)

        st.subheader("Translated Text")
        st.write(translated)

        if output_as_audio:
            with st.spinner("Generating speech..."):
                audio_path = text_to_speech(translated, language=target_lang, play_audio=False)
            st.audio(audio_path)