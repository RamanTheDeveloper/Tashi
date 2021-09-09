import datetime
import os
import webbrowser

import pyjokes
import pyttsx3
import pyaudio
import speech_recognition as sr
import wikipedia

voicename = "Tashi"

engine = pyttsx3.init()
voices = engine.getProperty("voices")
# engine.setProperty("voice", voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greetMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning sir")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon sir")
    else:
        speak("Good evening sir")
    speak("How can i assist you today")


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Trying to recognize your voice...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return query


if __name__ == "__main__":
    clear = lambda: os.system("cls")

    # Clean any command before execution of this Python file
    clear()
    greetMe()

    while True:
        query = takeCommand().lower()

        # Store all commands said by user in query
        if 'wikipedia' or 'tell me more about' in query:
            speak('Searching Wikipedia')
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("% I:% M:% %p")
            speak(f"Sir, the time is {strTime}")
        elif 'how are you' in query:
            speak("I am fine, Thank you")
        elif "what's your name" in query or "What is your name" in query:
            speak("My name is " + voicename)
        elif 'exit' in query:
            speak("Exiting system. Goodbye")
            exit()
        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Ramandeep Singh.")
        elif 'joke' in query:
            speak(pyjokes.get_joke())
