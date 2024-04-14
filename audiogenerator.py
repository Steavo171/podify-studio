from gtts import gTTS
import pyttsx3


def text_to_audio_gtts(text: str, language: str = 'en', output_file: str = 'output.mp3', tld="com"):

    tts = gTTS(text=text, lang=language, tld=tld)

    tts.save(output_file)
    print(f"Text converted to speech and saved as '{output_file}'")


def text_to_audio_pyttsx3(text: str, language: str = 'en', output_file: str = 'output.mp3'):

    engine = pyttsx3.init()

    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 0.9)  # Volume level

    engine.setProperty('language', language)

    engine.save_to_file(text, output_file)

    engine.runAndWait()

    print(f"Text converted to speech and saved as '{output_file}'")
