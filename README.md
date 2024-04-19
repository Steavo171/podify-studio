# Podify Studio

Podify Studio is a Python application for generating podcasts by merging text-based dialogs into audio files. It provides functionalities to convert text to speech using different text-to-speech (TTS) engines, merge audio files, and generate podcasts seamlessly.

## Features

- Convert text to speech using gTTS (Google Text-to-Speech) and pyttsx3.
- Generate multiple audio files from text-based dialogs.
- Merge audio files to create a podcast.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/AniruddhaGawali/podify-studio
   ```

2. Navigate to the project directory:

   ```bash
   cd podify-studio
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Install
   You can open and save WAV files with pure python. For opening and saving non-wav files – like mp3 – you'll need ffmpeg or libav. (for pydub)

## Usage

1. Prepare your text-based dialogs in a file, with each dialog formatted as `<name>:<text>`, separated by a delimiter (default is ';'). For example:

   ```
   Speaker 1: Hello, how are you?;
   Speaker 2: I'm fine, thank you!;
   Speaker 1: That's great!;
   ```

2. Use the provided Python scripts to generate audio files and merge them into a podcast:

   ```bash
   # Convert text to audio files using gTTS
   python text_to_audio_gtt.py --input dialogs.txt --output_folder output

   # Merge audio files into a podcast
   python generate_podcast.py --input_folder output --output podcast.mp3
   ```
