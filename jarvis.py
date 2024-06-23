import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
machine = pyttsx3.init()

def talk(text):
    machine.say(text)
    machine.runAndWait()

def input_instruction():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            instruction = listener.recognize_google(voice).lower()
            if "jarvis" in instruction:
                instruction = instruction.replace("jarvis", "")
                print(instruction)
            return instruction
    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        return ""

def play_jarvis():
    instruction = input_instruction()
    if instruction:
        print(instruction)
        if "play" in instruction:
            song = instruction.replace('play', '').strip()
            talk("playing " + song)
            pywhatkit.playonyt(song)
        elif "time" in instruction:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk("The current time is " + time)
        elif "date" in instruction:
            date = datetime.datetime.now().strftime("%d/%m/%Y")
            talk("Today's date is " + date)
        elif "how are you" in instruction:
            talk("I am fine, thank you.")
        elif "what is your name" in instruction:
            talk("My name is Jarvis, your virtual assistant.")
        elif "who is" in instruction:
            person = instruction.replace("who is", "").strip()
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
        else:
            talk("Please repeat the command.")
    else:
        talk("No instruction received.")

play_jarvis()
