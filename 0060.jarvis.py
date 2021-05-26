import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak('I am Jarvis, your personal assistant sir, please tell me how may I help you?')

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
