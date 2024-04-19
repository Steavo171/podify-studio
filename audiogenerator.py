from gtts import gTTS
import pyttsx3
from typing import Dict
from type import DialogListType,AudioSegmentType
import os
from audiomerger import mergeTwoAudio   
from pydub import AudioSegment


def textToAudioGtts(text: str, language: str = 'en', output_file: str = 'output.mp3', tld="com"):

    tts = gTTS(text=text, lang=language, tld=tld)

    tts.save(output_file)
  

def textToAudioPyttsx3(text: str, language: str = 'en', output_file: str = 'output.mp3'):

    engine = pyttsx3.init()

    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 0.9)  # Volume level

    engine.setProperty('language', language)

    engine.save_to_file(text, output_file)

    engine.runAndWait()

def generateMultiAudio(dialogs:DialogListType, language: str = 'en', output_folder: str = '/output',tld:Dict=None):
   
    if tld is None or len(dialogs)==0:
       return


    if not os.path.exists(output_folder):
        os.mkdir(output_folder)


    
    for i, dialog in enumerate(dialogs):
        name, text = dialog["name"], dialog["text"]
        output_file = f"{output_folder}/{i+1}.mp3"
        
        textToAudioGtts(text, language=language, output_file=output_file, tld=tld[name])



def generatePodcast(output_folder: str = '/output',len:int=0):

    podcast:AudioSegmentType = None
    for i in range(0,len):
        output_file:AudioSegmentType= AudioSegment.from_file(f"{output_folder}/{i+1}.mp3")
        if i == 0:
            podcast = output_file
        else:
            podcast = mergeTwoAudio(podcast,output_file)
        


    return podcast
        



    




#  for i, text in enumerate(texts):
#         name, text = text.split(":")
#         output_file = f"./audio/temp/{i+1}.mp3"

#         if (name.strip() == "Host"):
#             text_to_audio_gtts(text, language='en', output_file=output_file)
#         else:
#             text_to_audio_gtts(text, language='en',
#                                output_file=output_file, tld="co.za")
