# pip install pyttsx3 SpeechRecognition pyaudio

import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()

def speak(text):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Change 1 to 0 if error
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio, language='en-in')
        print("You said:", command)
        return command.lower()

    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        speak("Sorry, I did not catch that. Please try again.")
        return ""

    except sr.RequestError:
        print("Sorry, speech service error.")
        speak("Sorry, my speech service is down.")
        return ""

speak("Hello! I am your Bhaai. How can I help you today Bhaai?")

while True:
    command = listen()

    if 'hi' in command:
        speak("Hello Bhaai! How are you Miya Bhaai?")

    elif 'python' in command:
        speak("Python is a great programming language!")

    elif 'your name' in command:
        speak("My name is Python, your personal assistant Bhaai.")

    elif 'psf50' in command:
        speak("11 members are present today Bhaai.")

    elif 'stop' in command or 'quit' in command or 'bye' in command:
        speak("Ok Ok Bhaai, Thanks Namaste!")
        break

    else:
        speak("Sorry, I didn't understand that. Please try again.")