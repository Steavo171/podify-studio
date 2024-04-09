from type import AudioSegmentType
from pydub import AudioSegment
from audiomerger import addIntro, addOutro, addBackgroundMusic


def main():

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
    audio = addOutro(outro, audio, length=10, crossFade=1)
    audio.export("./audio/output.mp3", format="mp3")


if __name__ == "__main__":
    main()
