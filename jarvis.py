from email.mime import audio
from http import HTTPStatus
from logging import exception
from winreg import QueryInfoKey
from pip import main
from win10toast import ToastNotifier
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import subprocess







engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voices',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning!")
    elif hour>12 and hour<18:
        speak("Good Afternoon!")
    elif hour>=18 and hour<20:
        speak("Good Evening!")
    else:
        speak("Good night")

    speak("Hello sir I am Jarvis. Please tell me how may I help you")

def takeCommand():
    ''' It take microphone input from user and return string output '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio =r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:  
        # print(e)

        print("Say that again please....")
        return "None"
    return query


if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
    #Logic foe executing task based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(result)
        elif 'hey assistant' in query.lower():
            print("Desktop assistant activated!")
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'open gmail' in query:
            webbrowser.open("gmail.com")

        elif 'open chrome' in query:
            webbrowser.open("chrome.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is{strTime}")
        
        elif 'play music' in query:
            lst = []
            for file in os.listdir('D:\\songs\\music.mp3'):
                if file.endswith('.mp3'):
                    lst.append(file)
            print(lst)
            name = random.choice(lst)
            print(name)
            os.startfile(os.path.join('D:\\songs\\music.mp3',name))

        elif 'open visual studio' in query:
            codePath = "C:\\Users\\THOR\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open microsoft team' in query:
            webbrowser.open("microsoft team.com")
            
        
        elif 'open figma' in query:
            spath = "C:\\Users\\THOR\\AppData\\Local\\Figma\\app-116.5.18\\Figma.exe"
            os.startfile(spath)
        elif 'open zoom' in query:
            zoompath = "C:\\Users\\THOR\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
            os.startfile(zoompath)
        elif 'open settings' in query:
            os.system("start ms-settings:")
        elif 'open file explorer' in query.lower():
            print("Opening File Explorer...")
            os.name == 'nt'
            os.system("explorer")
        elif 'open wordfile' in query.lower():
            filepath = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk"
            subprocess.Popen(["start", filepath], shell=True)
            message = "Opening the Word file."
        
            