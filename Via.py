import speech_recognition as sr
import wikipedia
import webbrowser
import requests
import os
import datetime
import time
import pyttsx3
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[1].id')
engine.setProperty('rate', 100)
def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<16:
        speak("Good Afternoon")
        print("Hello,  Good Afternoon")
    else:
        speak("Good Evening")
        print("Hello, Good Evening")


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=5)
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='eng')
            print("You said:", statement,"\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement
    
print("Loading your AI personal assistant")
speak("Hi,  I,  am,  your,  personal,  assistant.")
wishMe()
if __name__=='__main__':


    while True:
        speak("Tell,  me,  how,  can,  I,  help,  you,  now?")
        statement = takeCommand().lower()
        if statement==0:
            continue
        
        if "good bye" in statement or "ok bye" in statement or "stop" in statement or "bye" in statement:
                    speak('your personal assistant v-one is shutting down,Good bye')
                    print('your personal assistant v-one is shutting down,Good bye')
                    break
                
        if 'wikipedia' in statement:
                    speak('Searching Wikipedia...')
                    statement =statement.replace("wikipedia", "")
                    results = wikipedia.summary(statement, sentences=3)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)

        elif 'open youtube' in statement:
                    webbrowser.open_new_tab("https://www.youtube.com")
                    speak("youtube is open now")
                    time.sleep(5)

        elif 'open google' in statement:
                    webbrowser.open_new_tab("https://www.google.com")
                    speak("Google chrome is open now")
                    time.sleep(5)
                    
        elif 'open gmail' in statement:
                    webbrowser.open_new_tab("https://www.gmail.com")
                    speak("Google Mail open now")
                    time.sleep(5)            
        elif 'time' in statement:
                    strTime=datetime.datetime.now().strftime("%H:%M:%S")
                    speak("the time is", strTime)

        elif 'news' in statement:
                    news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines”")
                    speak('Here are some headlines from the Times of India,Happy reading')
                    time.sleep(6)

        elif "camera" in statement or "take a photo" in statement:
                    ec.capture(0,"robo camera","img.jpg")
                    
        elif 'search'  in statement:
                    statement = statement.replace("search", "")
                    webbrowser.open_new_tab(statement)
                    time.sleep(5)            

        elif 'ask' in statement:
                    speak('I can answer to computational and geographical questions  and what question do you want to ask now')
                    question=takeCommand()
                    app_id="Paste your unique ID here "
                    client = wolframalpha.Client('R2K75H-7ELALHR35X')
                    res = client.query(question)
                    answer = next(res.results).text
                    speak(answer)
                    print(answer)

        elif 'who are you' in statement or 'what can you do' in statement:
                    speak('I am V-one version 1 point O your personal assistant. I am programmed to minor tasks like'
                          'opening youtube,google chrome, gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                          'In different cities, get top headline news from times of india and you can ask me computational or geographical questions too!')


        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
                    speak("I was built by legends")
                    print("I was built by the Tripathis")
                
                    
        elif "weather" in statement:
                    api_key="Apply your unique ID"
                    base_url="https://api.openweathermap.org/data/2.5/weather?"
                    speak("what is the city name")
                    city_name=takeCommand()
                    complete_url=base_url+"appid="+api_key+"&q="+city_name
                    response = requests.get(complete_url)
                    x=response.json()
                    if x["cod"]!="404":
                        y=x["main"]
                        current_temperature = y["temp"]
                        current_humidiy = y["humidity"]
                        z = x["weather"]
                        weather_description = z[0]["description"]
                        speak(" Temperature in kelvin unit is " +
                              str(current_temperature) +
                              "\n humidity in percentage is " +
                              str(current_humidiy) +
                              "\n description  " +
                              str(weather_description))
                        print(" Temperature in kelvin unit = " +
                              str(current_temperature) +
                              "\n humidity (in percentage) = " +
                              str(current_humidiy) +
                              "\n description = " +
                              str(weather_description))

                        
        elif "log off" in statement or "sign out" in statement:
                    speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
                    subprocess.call(["shutdown", "/l"])

        elif "what" in statement or "how" in statement or "when" in statement or "where" in statement or "who" in statement:
                    speak("showing search results by google" or "showing web results")
                    url = ("https://www.google.com.tr/search?q=", statement)  
                    webbrowser.open(url)
        
    

        elif "update yourself"  in statement or "self update" in statement or "update" in statement:
                    speak (" restarting for update")
                    print("....")
                    time.sleep(7)
                    import pers_AI

        elif "why" and "you" in statement:
            speak("my name is Iva , which ,means, Ishanya - Ved , personal assisant")  
                    
                        
                                
        time.sleep(3)
