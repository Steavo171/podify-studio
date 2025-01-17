from type import AudioSegmentType
from pydub import AudioSegment
from audiomerger import addIntro, addOutro, addBackgroundMusic
from audiogenerator import generateMultiAudio,generatePodcast
from utils import readTextFromFile, dialogListFromText


def text_to_speech():
    print("Welcome to Text-to-Speech Converter!")
    print("Choose the library you want to use:")
    print("1. gTTS (Google Text-to-Speech)")
    print("2. pyttsx3")

    choice = input("Enter your choice (1 or 2): ")

    text = ""
    if choice in ['1', '2']:
        text_source = input(
            "Enter '1' to enter text manually or '2' to read from a file: ")
        if text_source == '1':
            text = input("Enter the text to convert to speech: ")
        elif text_source == '2':
            file_path = input("Enter the path to the text file: ")
            text = read_text_from_file(file_path)
        else:
            print("Invalid choice. Please enter '1' or '2'.")

    language = input("Enter the language code (e.g., 'en' for English): ")
    output_file = input("Enter the output file name: ")

    if choice == '1':
        text_to_audio_gtts(text, language, output_file)
    elif choice == '2':
        text_to_audio_pyttsx3(text, language, output_file)
    else:
        print("Invalid choice. Please enter 1 or 2.")


def intro_outro():

    audio: AudioSegmentType = AudioSegment.from_file("./audio/test.mp3")

    choose = input("Do you want to add background music? (y/n): ")
    if choose == "y":
        background = AudioSegment.from_file("./audio/background.mp3")
    else:
        background = None

    choose = input("Do you want to add intro? (y/n): ")
    if choose == "y":
        intro = AudioSegment.from_file("./audio/intro.mp3")
    else:
        intro = None

    choose = input("Do you want to add outro? (y/n): ")
    if choose == "y":
        outro = AudioSegment.from_file("./audio/outro.mp3")
    else:
        outro = None

    audio = addBackgroundMusic(
        background, audio, loop=True, volumn=10, postion=0)
    audio = addIntro(intro, audio, length=5, crossFade=1)
    audio = addOutro(outro, audio, length=8, crossFade=1)
    audio.export("./audio/output.mp3", format="mp3")


def multiperson():
    print("Welcome to Multi-person Audio Generator!")
    print("Enter the text for each person separated by a semicolon (;).")
    print("For example, 'Person 1: Hello; Person 2: Hi'")

    pathOfText=input("Enter the path of the text file: ")


    text = readTextFromFile(pathOfText)
    dilogs = dialogListFromText(text)
    print("Generating audio...")
    generateMultiAudio(dilogs, language="en", output_folder="./audio/temp",tld={"Host":"com","Co-Host":"co.uk"})

    print("Combining all audios...")
    podcast = generatePodcast(output_folder="./audio/temp",len=len(dilogs))
    podcast.export("/output.mp3", format="mp3")
    


if __name__ == "__main__":
    multiperson()
