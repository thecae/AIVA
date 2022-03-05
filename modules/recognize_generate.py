import speech_recognition
from gtts import gTTS
from playsound import playsound


def listen():
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


filename = "test_response.mp3"


def generate_audio(string):
    audio = gTTS(string)
    audio.save("../audio_files/" + filename)
    playsound("../audio_files/" + filename)
