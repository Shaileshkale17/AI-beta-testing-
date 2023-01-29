import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import pyautogui
from pyautogui import click
from time import sleep



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id) - the check in voice

engine.setProperty('voice', voices[0].id)
cordinates = pyautogui.position()
def bluetooth_automation():
    pyautogui.click(x=1892 , y=1067)
    sleep(2)
    pyautogui.click(x=1756 , y=724)
    sleep(1)
    pyautogui.hotkey('win','k')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('enter')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour==0 and hour==12:
     speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good afternoon!")
    else:
        speak("Good Evening!")

    speak("I am beta testing 2.5 . please tall me how may I help you")

def takeCommand():
    # it takes microphone input from the user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
     print("Listening....")
     r.pause_threshold = 0.8
     audio = r.listen(source)

    try:
        print("recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said :{query}\n")
    except Exception as e :
        # print(e) display the Error
        print("say that again please....")
        return "None"
    return query
# This function is not be used 
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('shailehkale042@gmail.com','password')
    server.sendmail('shaileshkale042@gmail.com', to, content)
    server.close()

if __name__ == '__main__':
    wishMe()
    # while True:
    if 1:
        query = takeCommand().lower()
        #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('searching wikipedia.....')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=10 )
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif'open youtube' in query:
            webbrowser.open("youtube.com")

        elif'open google' in query:
            googlePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google chrome"
            os.startfile(googlePath)

        elif'open firefox' in query:
            firefoxPath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Firefox"
            os.startfile(firefoxPath)

        elif'open firefox' in query:
            firefoxPath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Edge"
            os.startfile(firefoxPath)

        elif'open xampp ' in query:
           xamppPath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\XAMPP" 
           os.startfile(xamppPath)
        
        elif'open firefox' in query:
           firefoxPath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Firefox"
           os.startfile(firefoxPath)

        elif'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif'open music' in query:
            music_dir = 'C:\\Users\\shail\\Music'
            # music_dir = 'C:\\Users\\shail\\Music\\music_beta'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M;%S")
            speak (f"Sir ,the timeis {strTime}")
        elif 'open code'in query:
            codePath = "C:\\Users\\shail\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs"
            os.startfile(codePath)
        elif 'open project file'in query:
            projectPath = "D:\\PROJECT"
            os.startfile(projectPath)
        elif 'email to shailesh' in query:
            try:
                speak("ehat should i say?")
                content = takeCommand()
                to = "shaileshyourEmail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry i can not sent the Email")
        elif'open bluetooth' in query:
            speak('okay i am open the bluetooth')
            bluetooth_automation()
        elif'quit' in query:
            speak('okay i am quit')
            
