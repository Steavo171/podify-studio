from pydub import AudioSegment

test = AudioSegment.from_file("intro.mp3")
test2 = AudioSegment.from_file("test.mp3")

first_10_seconds = test[:10000]

test3 = test2.overlay(test, position=0, gain_during_overlay=10)
test3.export("test3.mp3", format="mp3")
