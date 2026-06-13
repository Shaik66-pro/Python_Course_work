#pip install . pyttsx3 SpeechRecognition 
import speech_recognition as sr
import pyttsx3


# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to make the assistant speak
def speak(text):
    voice = engine.getProperty('voices')  # You can change the index to select a different voice
    engine.setProperty('voice', voice[1].id)
    engine.say(text)
    engine.runAndWait()
    
# Function to listen for user voice

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio,language='en-in')
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        speak("Sorry, I did not catch that. Please try again.")
        return ""
    except sr.RequestError:
        print("Sorry, my speech service error.")
        speak("Sorry, my speech service is down.")
        return ""
    
speak("Hello! I am your AI Assistant. How can I help you today AI Assistant?. you can ask me anything Sameer!")
while True:
    command = listen()
    
    if 'hi' in command:
        speak("Hello Sameer! How are you?")
    elif 'python' in command:
        speak("Python is a great programming language!")
    elif 'your name' in command:
        speak("My name is Python, your personal assistant Sameer.")
    elif 'psf50' in command:
        speak("11 members are present today Sameer.")
    elif 'stop' in command or 'quit' in command or 'bye' in command:
        speak("Ok Ok Sameer, Thanks Namaste!")
        break
    else:
        speak("Sorry, I didn't understand that. Please try again.")
        