# PyJarvis
A personal assistant made in python which follows some basic commands and can be improved
---
For using jarvis you need to install some libraries
1. pyttsx3
2. speech_recognition
3. wikipedia
---
The rest of the packages need not be installed:
1. datetime
2. webbrowser

So, first we need to import these packages..
```
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
```
So now we initialize pyttsx3
```
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
```
To make a assistant its very important that the assistant speaks, so now we make the speak function..
```
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
```
Now we make a greeting function which wishes us each time we run the program according to the time..
```
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak('I am Jarvis, your personal assistant sir, please tell me how may I help you?')
```
The assistant should also take commands from us, so for that we need to use to use speech_recognition library to make another method
```
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please..")
        return "None"
    return query
 ```
 And now the functional part..
 ```
 if __name__ == "__main__" :
    wishMe()
    while True:
        query = takeCommand().lower()
        if "wikipedia" in query:
            speak('Searching wikipedia..')
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=2)
            speak('According to wikipedia: ')
            print(results)
            speak(results)
        elif 'open youtube' in query:
            speak('opening youtube')
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            speak('opening google')
            webbrowser.open('google.com')
            webbrowser.open('web.whatsapp.com')
        elif 'bye' in query:
            speak('bye sir')
            quit()
```
This is the simple program I hope you understood it..
