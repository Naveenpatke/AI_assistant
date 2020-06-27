import sounddevice as sd
import speech_recognition as sr
import main  # patke module to import speak function
import wavio  # helps in converting recorded audio in wav format


def record(duration):
    # This function records audio from the microphone and the saves in the audio in wav format
    fs = 44100  # Sample rate
    seconds = duration  # Duration of recording
    print("Listening...")
    print("Say something!")
    my_recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    wavio.write('output.wav', my_recording, fs, sampwidth=2)  # saving the recorded audio and renaming it as output.wav


def listen_command():
    # This function helps in recognizing the command present in the audio file
    record(6)
    r = sr.Recognizer()  # initiating the recognizer
    voice = sr.AudioFile('output.wav')  # reading the audio file
    with voice as source:
        r.pause_threshold = 1.5  # amount of non-speaking time before the recorded voice to consider it as phase(chunk)
        r.energy_threshold = 690  # minimum amount of energy in voice to be considered as valid voice
        r.adjust_for_ambient_noise(source)
        audio = r.record(source)
        query = "null"
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en")
        print("user said:" + query)

    except sr.UnknownValueError:
        print("Sorry for the inconvenience, Can you say it again sir...")
        main.speak("Sorry for the inconvenience, Can you say it again sir...")
        return "null"

    except sr.RequestError:
        main.speak("Sir your not connected to internet, so i cant process your request")

    return query


def listen_main_command():
    # This function helps in recognizing the command present in the audio file
    record(6)
    r = sr.Recognizer()  # initiating the recognizer
    voice = sr.AudioFile('output.wav')  # reading the audio file
    with voice as source:
        r.pause_threshold = 1.5  # amount of non-speaking time before the recorded voice to consider it as phase(chunk)
        r.energy_threshold = 690  # minimum amount of energy in voice to be considered as valid voice
        r.adjust_for_ambient_noise(source)
        audio = r.record(source)
        query = "null"
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en")

    except sr.UnknownValueError:
        return "null"

    except sr.RequestError:
        main.speak("Sir your not connected to internet, so i cant process your request")

    return query


def listen_command1():
    record(1)
    r = sr.Recognizer()  # initiating the recognizer
    voice = sr.AudioFile('output.wav')  # reading the audio file
    with voice as source:
        r.pause_threshold = 1.5  # amount of non-speaking time before the recorded voice to consider it as phase(chunk)
        r.energy_threshold = 690  # minimum amount of energy in voice to be considered as valid voice
        r.adjust_for_ambient_noise(source)
        audio = r.record(source)
        query = "null"
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en")

    except sr.UnknownValueError:
        return "null"

    except sr.RequestError:
        main.speak("Sir your not connected to internet, so i cant process your request")

    return query
