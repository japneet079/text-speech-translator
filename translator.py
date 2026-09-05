"""Handles language detection and text translation."""

from googletrans import Translator
from langdetect import detect, DetectorFactory, LangDetectException

DetectorFactory.seed = 0

# One shared Translator instance for the whole app
_translator = Translator()


def detect_language(text: str) -> str:
    """Detect the language of the given text. Returns 'unknown' if it can't."""
    cleaned_text = text.strip()
    if not cleaned_text:
        return "unknown"
    try:
        return detect(cleaned_text)
    except LangDetectException:
        return "unknown"


def translate_text(text: str, target_lang: str, source_lang: str = "auto") -> str:
    """Translate text into the target language using Google Translate (via googletrans)."""
    cleaned_text = text.strip()
    if not cleaned_text:
        return ""

    result = _translator.translate(cleaned_text, dest=target_lang, src=source_lang)
    return result.text