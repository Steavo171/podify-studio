from type import AudioSegmentType


def addIntro(intro: AudioSegmentType, audio: AudioSegmentType, length: int = None, crossFade: int = .1) -> AudioSegmentType:
    """
  This function adds an intro audio file to another audio file.

  Args:
      intro:
        Path to the intro audio file (str).

      audio: 
        Path to the audio file to add intro to (str).

      length:
        The length of the intro to add (int) in sec.crossFade: The crossfade duration (int) in sec.

      crossFade: 
        The crossfade duration (int) in sec.

  Returns:
      A new AudioSegment object with the intro added to the beginning (AudioSegment).
  """
    if (intro is None):
        return audio

    intro = intro[:length*1000]
    audio: AudioSegmentType = intro.append(audio, crossfade=crossFade*1000)
    return audio


def addOutro(outro: AudioSegmentType, audio: AudioSegmentType, length: int = None, crossFade: int = .1) -> AudioSegmentType:
    """
  This function adds an outro audio file to another audio file.

  Args:
      outro:
        Path to the outro audio file (str).

      audio:
        Path to the audio file to add outro to (str).

      length:
        The length of the outro to add (int) in sec.

      crossFade:
        The crossfade duration (int) in sec.

  Returns:
      A new AudioSegment object with the outro added to the end (AudioSegment).
  """

    if (outro is None):
        return audio

    outro = outro[:length*1000]
    audio = audio.append(outro, crossfade=crossFade*1000)
    return audio


def addBackgroundMusic(background: AudioSegmentType, audio: AudioSegmentType, loop: bool = False, volumn: int = None, postion: int = 0) -> AudioSegmentType:
    """
  This function adds background music to another audio file.

  Args:
      background:
        Path to the background music audio file (str).

      audio:
        Path to the audio file to add background music to (str).

      loop:
        Whether the background music should loop (bool).

      volumn:
        The volume of the background music (int).

      postion:
        The position to start the background music (int) in sec.


  Returns:
      A new AudioSegment object with the background music added (AudioSegment).
  """
    if (background is None):
        return audio

    audio = audio.overlay(
        background, gain_during_overlay=volumn, position=postion*1000, loop=loop)
    return audio
