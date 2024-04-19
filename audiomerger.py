from type import AudioSegmentType


def addIntro(intro: AudioSegmentType, audio: AudioSegmentType, length: int = None, crossFade: int = .1) -> AudioSegmentType:
    """
    This function adds an intro audio file to another audio file.

    Args:
        intro:
            The intro audio segment (AudioSegmentType).

        audio: 
            The main audio segment (AudioSegmentType) to which the intro will be added.

        length:
            The length of the intro to add in seconds (int). If None, the entire intro is used.

        crossFade: 
            The crossfade duration in seconds (float).

    Returns:
        A new AudioSegment object with the intro added to the beginning.
    """

    if intro is None:
        return audio

    # Trim intro if length is provided
    intro = intro[:length * 1000]
    
    # Append intro to audio with crossfade
    audio = intro.append(audio, crossfade=crossFade * 1000)
    return audio


def addOutro(outro: AudioSegmentType, audio: AudioSegmentType, length: int = None, crossFade: int = .1) -> AudioSegmentType:
    """
    This function adds an outro audio file to another audio file.

    Args:
        outro:
            The outro audio segment (AudioSegmentType).

        audio:
            The main audio segment (AudioSegmentType) to which the outro will be added.

        length:
            The length of the outro to add in seconds (int). If None, the entire outro is used.

        crossFade:
            The crossfade duration in seconds (float).

    Returns:
        A new AudioSegment object with the outro added to the end.
    """

    if outro is None:
        return audio

    # Trim outro if length is provided
    outro = outro[:length * 1000]
    
    # Append outro to audio with crossfade
    audio = audio.append(outro, crossfade=crossFade * 1000)
    return audio


def addBackgroundMusic(background: AudioSegmentType, audio: AudioSegmentType, loop: bool = False, volume: int = None, position: int = 0) -> AudioSegmentType:
    """
    This function adds background music to another audio file.

    Args:
        background:
            The background music audio segment (AudioSegmentType).

        audio:
            The main audio segment (AudioSegmentType) to which the background music will be added.

        loop:
            Whether the background music should loop (bool).

        volume:
            The volume of the background music (int).

        position:
            The position in seconds to start the background music (int).

    Returns:
        A new AudioSegment object with the background music added.
    """

    if background is None:
        return audio

    # Overlay background music on audio
    audio = audio.overlay(
        background, gain_during_overlay=volume, position=position * 1000, loop=loop)
    return audio


def mergeTwoAudio(audio1: AudioSegmentType, audio2: AudioSegmentType) -> AudioSegmentType:
    """
    This function merges two audio segments together.

    Args:
        audio1:
            The first audio segment (AudioSegmentType).

        audio2:
            The second audio segment (AudioSegmentType).

    Returns:
        A new AudioSegment object containing the merged audio segments.
    """

    return audio1 + audio2
