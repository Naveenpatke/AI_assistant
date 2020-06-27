import pyttsx3   # this module is used to install the sapi5 package to convert text to speech
# to access the build in voices in windows OS
import datetime  # this module is used to access the current time and date from the system
import os
import queries
import aiml

engine = pyttsx3.init('sapi5')  # this line initialise the sapi5 module to variable named as engine
voices = engine.getProperty('voices')  # this line is used to get all the builtin voices present in the windows os
engine.setProperty('voice', voices[1].id)  # this line is used to set the desired voice among the available voices


def wish_me():
    # this function is used to wish the owner of the AI
    hour = int(datetime.datetime.now().hour)
    if 0 < hour < 12:
        speak("Good Morning Sir")
    elif 12 <= hour < 17:
        speak("Good Afternoon Sir")
    elif 17 <= hour < 20:
        speak("Good Evening Sir")
    else:
        speak("Good night sir")

    speak("My name is Maggi")


def speak(audio):
    # this function helps in converting the text into speech
    engine.say(audio)
    engine.runAndWait()


def train_maggi():
    kernel = aiml.Kernel()
    if os.path.isfile("bot_brain.brn"):
        kernel.bootstrap(brainFile="bot_brain.brn")
    else:
        kernel.bootstrap(learnFiles="std-startup.xml", commands="load aiml b")
        # kernel.saveBrain("bot_brain.brn")
    return kernel


if __name__ == "__main__":
    kernel_brain = train_maggi()
    # key_word = recognize_voice.listen_main_command().lower()
    queries.activate_maggi(kernel_brain)
    # while True:
    #     if "Hey maggi" in key_word or "maggi" in key_word or "hey" in key_word:
    #         wish_me()
    #         queries.activate_maggi()
    #     key_word = recognize_voice.listen_main_command().lower
