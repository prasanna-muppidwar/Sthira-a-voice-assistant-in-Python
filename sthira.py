
import shutil
from urllib import response
import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser

import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def username():
    speak("What should i call you ")
    uname = takeCommand()
    speak("Welcome ")
    speak(uname)
    columns = shutil.get_terminal_size().columns
     
    
    print("Welcome", uname.center(columns))
  
     
    speak("How can i Help you, Sir")
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Sthira Activated!")
        speak(" Good Morning Sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")   

    else:
        speak("Good Evening!")  

    speak("How May I help You?")       

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)                 

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query----------------------------------------------------------
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            #time--------------
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'reminders' in query:
            print(f"reminders : Complete your java Course \tGo to Bank \t Drink wter ")
            speak(f"Complete your java Course")
            speak(f"Go to Bank")
            speak(f" Drink enough water")

          #Accu weather 
        elif'current temperature' in query:
            webbrowser.open("accuweather.com")   
            speak(f"here u go")
          #Open Youtube
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")
            speak(f"here you go happy watching...")
        elif 'open google' in query:
            webbrowser.open("google.com")
            speak(f"Done Sir...")
        elif 'open github' in query:
            webbrowser.open("https://github.com/prasanna-muppidwar")   
        elif 'show some news' in query:
            webbrowser.open("https://www.bbc.com/")
            speak(f"page opened successfully...")

       #my basic
        elif 'open my java course' in query:
            webbrowser.open("https://www.youtube.com/playlist?list=PLu0W_9lII9agS67Uits0UnJyrYiXhDS6q")  
        elif 'open canva' in query:
            webbrowser.open("https://www.canva.com/")  
        elif 'open colour palette' in query:
            webbrowser.open("https://coolors.co/")  
        elif 'w3school how to' in query:
            webbrowser.open("https://www.w3schools.com/howto/")
        elif 'my projects' in query:
            webbrowser.open("https://www.w3schools.com/howto/")

        #about sthira
        
        elif 'your name' in query:
            speak(f"Sir my name is sthira")
        elif 'your date of birth' in query:
            speak(f"18 April")
        elif 'your gender' in query:
            speak(f" Im  a wonder girl")
        elif 'tell me something about you' in query:
            speak(f"My name is Sthira a voice assistant")
        

 #basic answering-----------------------------------------------------------------------------
        elif 'you there' in query:
            speak(f"Yes Im Always there for You")
        elif 'how are you' in query:
            speak(f"Im doing great, what about you")
        elif 'good morning' in query:
            speak(f"Good morning Prasanna")
        elif 'good afternoon' in query:
            speak(f"Good Afternoon Prasanna")
        elif 'thank you' in query:
            speak(f"you re welcome")
        elif 'alexa' in query:
            speak(f"you Bitch, Im Sthira")
            speak(f"Shut the Fuck Up")
        elif 'tell me something' in query:
            speak(f"Are you a candle? Because you’re so hot of the looks with you.")
        elif 'ok'+'yes' in query:
            speak(f"cool")
        elif 'will you marry me' in query:
            speak(f"no i wont i am loyal to prasanna")
        elif 'do you like humans' in query:
            speak(f"Yes i like humans")
         
       
            
