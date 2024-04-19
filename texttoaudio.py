# Import necessary modules and types
from type import AudioSegmentType, DialogListType
from typing import Dict, List
import os

# Importing libraries for text-to-speech conversion
from pydub import AudioSegment  # For audio processing
from gtts import gTTS  # Google Text-to-Speech API
import pyttsx3  # For text-to-speech conversion using pyttsx3 engine

# Function to convert text to speech using gTTS (Google Text-to-Speech)
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

# Function to convert text to speech using pyttsx3 engine
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

# Class to handle text-to-podcast conversion
class TextToPodcast:
    def __init__(self):
        self.podcast_name = ""  # Name of the podcast
        self.script = ""  # Script for the podcast
        self.output_folder = ""  # Output folder for the generated podcast
        self._podcast: AudioSegmentType = None  # Final podcast audio

        self.intro: AudioSegmentType = None  # Introductory audio segment
        self.outro: AudioSegmentType = None  # Concluding audio segment
        self.background_music: AudioSegmentType = None  # Background music for the podcast

        self._dialogs: DialogListType = []  # List to store dialogues from the script
        self._dialogs_audio: List[AudioSegmentType] = []  # List to store audio segments for each dialogue
        self.person_audio: Dict[str, str] = None  # Dictionary to map person names to their respective TLDs

    # Set the script for the podcast
    def set_script(self, text: str = None, path: str = None):
        if path:
            with open(path, "r") as f:
                self.script = f.read()
        elif text:
            self.script = text
        else:
            raise ValueError("Please provide either a text or a path to the script file")

    # Set the name of the podcast
    def set_podcast_name(self, name: str):
        self.podcast_name = name

    # Set the output folder for the generated podcast
    def set_output_path(self, folder: str):
        self.output_folder = folder
    
    # Set the introductory audio segment
    def set_intro(self, intro: AudioSegmentType):
        self.intro = intro
    
    # Set the concluding audio segment
    def set_outro(self, outro: AudioSegmentType):
        self.outro = outro

    # Set the background music for the podcast
    def set_background_music(self, music: AudioSegmentType):
        self.background_music = music
    
    # Set the mapping of person names to their respective TLDs
    def set_person_audio(self, person_audio: Dict[str, str]):
        self.person_audio = person_audio

    # Extract unique person names from the script
    def get_person_from_script(self) -> List[str]:
        persons: List[str] = []
        for i, dialog in enumerate(self._dialogs):
            name = dialog["name"]
            if name not in persons:
                persons.append(name)
        return persons
    
    # Split the script into individual dialogues
    def _split_in_dialogs_from_script(self):
        dialogs = self.script.replace("\n", "").strip().split(";")
        dialogs = [dialog.strip() for dialog in dialogs]

        dialogsList: DialogListType = []

        # Remove the last empty element if present
        if dialogs[-1] == '':
            dialogs.pop()

        # Parse each dialog and append it to the dialogsList
        for dialog in dialogs:
            name, text = dialog.split(":")
            dialogsList.append({"name": name, "text": text})

        self._dialogs = dialogsList

    # Generate audio segments for each dialogue in the script
    def _generate_audio_from_dialogs(self):
        self._split_in_dialogs_from_script()
        
        for i, dialog in enumerate(self._dialogs):
            name, text = dialog["name"], dialog["text"]
            output_file = f"{self.output_folder}/dialog.mp3"
            textToAudioGtts(text, tld=self.person_audio[name], output_file=output_file)
            audio = AudioSegment.from_file(output_file)
            self._dialogs_audio.append(audio)
        
        os.remove(f"{self.output_folder}/dialog.mp3")

    # Generate the final podcast by combining all audio segments
    def generate_podcast(self):
        self._generate_audio_from_dialogs()
        self._podcast = self._dialogs_audio[0]

        for i in range(1, len(self._dialogs_audio)):
            self._podcast = self._podcast + self._dialogs_audio[i]

        if self.background_music:
            self._podcast = self.background_music.overlay(self._podcast)

        if self.intro:
            self._podcast = self.intro + self._podcast

        if self.outro:
            self._podcast = self._podcast + self.outro

        self._podcast.export(f"{self.output_folder}/{self.podcast_name}_output.mp3", format="mp3")

# Example usage
podcast = TextToPodcast()
podcast.set_podcast_name("My Podcast")
podcast.set_script(path="./test.txt")
podcast.set_person_audio({"Host": "com", "Co-Host": "co.za"})
podcast.set_output_path("./audio")
podcast.generate_podcast()
