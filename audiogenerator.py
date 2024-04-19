from gtts import gTTS
import pyttsx3
from typing import Dict
from type import DialogListType, AudioSegmentType
import os
from audiomerger import mergeTwoAudio
from pydub import AudioSegment


def textToAudioGtts(text: str, language: str = 'en', output_file: str = 'output.mp3', tld="com"):
    """
    Convert text to speech using gTTS (Google Text-to-Speech) and save it as an audio file.

    Args:
        text: 
            The input text to convert to speech (str).

        language: 
            The language of the input text (str).

        output_file: 
            The path to save the output audio file (str).

        tld:
            Top-level domain (TLD) for the Google TTS service (str).

    Returns:
        None
    """
    tts = gTTS(text=text, lang=language, tld=tld)
    tts.save(output_file)


def textToAudioPyttsx3(text: str, language: str = 'en', output_file: str = 'output.mp3'):
    """
    Convert text to speech using pyttsx3 and save it as an audio file.

    Args:
        text: 
            The input text to convert to speech (str).

        language: 
            The language of the input text (str).

        output_file: 
            The path to save the output audio file (str).

    Returns:
        None
    """
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 0.9)  # Volume level
    engine.setProperty('language', language)
    engine.save_to_file(text, output_file)
    engine.runAndWait()


def generateMultiAudio(dialogs: DialogListType, language: str = 'en', output_folder: str = '/output', tld: Dict = None):
    """
    Generate multiple audio files from a list of dialogs using gTTS.

    Args:
        dialogs: 
            List of dictionaries containing dialog information (DialogListType).

        language: 
            The language of the dialogs (str).

        output_folder: 
            The folder path to save the generated audio files (str).

        tld:
            Top-level domain (TLD) for the Google TTS service (Dict).

    Returns:
        None
    """
    if tld is None or len(dialogs) == 0:
        return

    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    for i, dialog in enumerate(dialogs):
        name, text = dialog["name"], dialog["text"]
        output_file = f"{output_folder}/{i+1}.mp3"

        textToAudioGtts(text, language=language, output_file=output_file, tld=tld[name])


def generatePodcast(output_folder: str = '/output', len: int = 0):
    """
    Generate a podcast by merging multiple audio files.

    Args:
        output_folder: 
            The folder path containing the audio files to merge (str).

        len:
            The number of audio files to merge (int).

    Returns:
        An AudioSegment object containing the merged podcast.
    """
    podcast: AudioSegmentType = None
    for i in range(0, len):
        output_file: AudioSegmentType = AudioSegment.from_file(
            f"{output_folder}/{i+1}.mp3")
        if i == 0:
            podcast = output_file
        else:
            podcast = mergeTwoAudio(podcast, output_file)

    return podcast
