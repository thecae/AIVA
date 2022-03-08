import speech_recognition
from gtts import gTTS
from pygame import mixer


def listen():
    """
    The listen function uses the speech_recognition class which is based on Google's
    dictation (speech recognition) API to convert audio strings into text.   If the
    function cannot process the message, it throws class-defined errors.

    :return: The search query from the user
    """

    recognizer = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        audio_input = recognizer.listen(source)
        try:
            data = recognizer.recognize_google(audio_input)
            return data
        except speech_recognition.UnknownValueError:
            generate_audio("I didn't catch what you said.")
        except speech_recognition.RequestError as error:
            generate_audio("I'm having trouble connecting: {}.".format(error))
    return False

    # temporary input in audioless space
    # search_query = input()
    # return search_query


# filename for output
filename = "query_response.mp3"


def generate_audio(string):
    """
    The generate function utilizes Google's Text-to-Speech API to turn strings into audio
    messages that are played back to the user.  The function also utilizes Pygame, a class
    that contains the functionality (via pygame.mixer) to play stored .mp3 files.  The TTS
    stores the .mp3 result into the directory and then pygame.mixer plays it.

    :param string: The string output for TTS
    """

    audio = gTTS(string)
    audio.save("../audio_files/" + filename)

    mixer.init()
    mixer.music.load("../audio_files/" + filename)
    mixer.music.play()

    # temporary output in audioless space
    # print(string)
