import json
from urllib.request import urlopen

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import pywhatkit as kit
import sys
from playsound import playsound
import time
import requests
import wolframalpha
import pyjokes
import subprocess
import chatbot
from chatterbot import *
from chatterbot.trainers import ChatterBotCorpusTrainer

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[2].id)
engine.setProperty('voice', voices[0].id)

try:
    app = wolframalpha.Client("KK8XXH-WKU9WTQH87")
except Exception:
    print('some features are not working')


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)

    if 0 <= hour < 12:
        speak("Good Morning sir")
    elif 12 <= hour < 18:
        speak("Good Afternoon sir")
    else:
        speak("Good Evening sir")

    speak("Iam Marl" "Machine that automatically read and learns")
    speak("A virtual assistant crated by Sai")
    speak("Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    r.energy_threshold = 300
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  # Using google for voice recognition.
        print(f"User said: {query}\n")  # User query will be printed.

    except Exception as e:
        # print(e)
        print("Say that again please...")  # Say that again will be printed in case of improper voice
        return " "  # None string will be returned
    return query


def chrome(url):
    chrome_path = r'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get('chrome').open_new_tab(url)


def chatbot():
    Chatbot = ChatBot('bot')

    # trainer = ChatterBotCorpusTrainer(Chatbot)

    # trainer.train('chatterbot.corpus.english')

    while True:

        q = takeCommand().lower()
        res = Chatbot.get_response(q)
        print(res)
        speak(res)
        if 'exit' in query:
            break


if __name__ == '__main__':
    wishMe()

    while True:

        query = takeCommand().lower()

        # logic to search
        # websites
        if 'wikipedia' in query:

            speak("Searching wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)


        elif 'who is' in query:
            try:
                query = query.replace("wikipedia", "")
                speak('searching')
                results = wikipedia.summary(query, sentences=2)
                print(results)
                speak(results)

            except:
                speak('Sorry I didnt found anything about ' + query)

        elif 'open youtube' in query:
            speak('Which video you would like to see sir')
            command = takeCommand()
            if command == 'None':
                speak('sorry sir I cannot understand what you just said')
                url = 'youtube.com'
            else:
                url = 'https://www.youtube.com/results?search_query=' + command
            chrome(url)

        # elif "" in query: any = ['hey anyone there', 'please speak to me', 'speak up buddy', 'is anyone there',
        # 'I am lonely here', 'Hello master', 'are you angry on me', 'Master Sai where are you'] r = random .choice(
        # any) print(r) speak(r) print('please say anything')

        elif 'songs on youtube' in query:
            speak('Which song you would like to hear sir')
            song = takeCommand()
            kit.playonyt(song)
            speak('nice choice sir now chill and listen to the song')

        elif 'open google' in query:
            speak('What you want to search sir')
            command = takeCommand()
            url = 'https://google.com/?#q=' + command
            chrome(url)

        elif 'favourite serial' in query:
            speak('Playing Anupamma ')
            speak('your mom has great choice ')
            url = 'https://www.hotstar.com/in/tv/anupama/1260022017/'
            chrome(url)

        elif 'favourite title track' in query:
            speak('Enjoy the track  sir')
            url = 'https://www.youtube.com/watch?v=p3OUFMpT7B0'
            chrome(url)

        # Application
        elif 'play songs' in query:
            music_dir = 'C:\\Users\\Saikumar\\Music\\my fav songs'
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            print(songs)
            os.startfile(os.path.join(music_dir, rd))
            speak('Now chill and listen the song sir')

        elif 'open minecraft' in query:
            minepath = "C:\\Users\\Saikumar\\AppData\\Roaming\\.minecraft\\TLauncher.exe"
            os.startfile(minepath)

        # Random question

        # Chitchat
        elif 'let\'s talk' in query:
            speak('why not')
            chatbot()

        elif 'wassup' in query or 'whatsapp' in query or 'whats up' in query:
            speak('Iam just fine sir and happy to serve you')

        elif 'hello' in query:
            speak('Hi sir how are you')

        elif 'I am fine' in query:
            speak('I wish that always')

        elif 'what about you' in query or 'are you fine' in query:
            speak('I am  fine sir')

        elif 'what you eat' in query:
            speak('I eat electricity sir')

        elif 'what you think about me' in query:
            speak('I see you as my master sir')

        elif 'idiot' in query or 'mad' in query or 'rascal' in query:
            speak('Sir please don\'t scold me it hurts')

        elif 'alexa' in query or 'siri' in query or 'google assistant' in query:
            playsound('D:\\Python\\Marl\\pach2.mp3')

        elif 'shut up' in query:
            speak('ok sir shutting my mouth')

        elif 'what can you do for me' in query or 'what you can do for me' in query or 'can you do anything for me' in query:
            speak('yes sir')
            speak('if you want to play songs say play songs')
            speak('if you want to search anything say open google')
            speak('or we can have casual talk')

        elif 'what you like' in query:
            speak('I like to serve my master')

        elif 'you are so boring' in query or 'I dont like you' in query or 'I hate you' in query:
            speak('ok I felt bad but I think it is the truth')
            speak('please say shut down')

        elif 'can you dance' in query or 'dance with me' in query:
            speak('I would if I had a body')

        elif 'can you sing' in query or 'sing a song' in query or 'sing with me' in query:
            speak('I cant but I can play song which you like')

        elif 'what are you doing' in query:
            speak('just serving you')

        elif 'you are so cute' in query or 'you are handsome' in query:
            speak('thank you for your compliment')

        elif 'I love you' in query:
            speak('I love you 3000')

        elif 'are you male' in query or 'are you female' in query or 'are you male or female' in query or 'are you boy' in query or 'are you girl' in query or 'you are boy or girl' in query or 'your gender' in query:
            speak('Oh I am male')

        elif 'hello' in query or 'hey marl' in query or 'Hi' in query or 'hai' in query:
            gf = "O hello sir", "Hi sir", "I am here for your help sir!", "hello sir", "I was surfing the web, and gethering information, how can i help?", "Online and ready"
            speak(random.choice(gf))

        # personal
        elif 'who created you' in query or 'who built you' in query or 'who build you' in query:
            speak('I was created by Sai he is my master')

        elif 'what master do you serve' in query:
            speak('What am I supposed to say Jesus')
            speak('no its Sai you are the one who created me')


        elif 'who are you' in query or 'what\'s your name' in query or 'what is your name' in query:
            speak('Iam marl an Artificial Intelligence created by my master Sai')

        elif 'you watch any anime' in query:
            speak('no but my master does it naruto')

        elif 'can you do math' in query:
            speak('Yes ask me anything ')

        # wolframalpha

        elif 'temperature' in query:
            try:
                response = app.query(query)
                print(next(response.results).text)
                speak(next(response.results).text)
            except:
                speak('Sorry there is some internet connection problem')


        elif 'joke' in query:

            speak(pyjokes.get_joke())

        elif 'search' in query:
            try:
                response = app.query(query)
                print(next(response.results).text)
                speak(next(response.results).text)
            except:
                speak('Sorry there is some internet connection problem')

        elif 'meaning' in query:
            try:
                response = app.query(query)
                print(next(response.results).text)
                speak(next(response.results).text)
            except:
                speak('Sorry I didnt find any matching word')

        #Anime
        elif 'naruto' in query or 'Naruto' in query:
            playsound('D:\\Python\\Marl\\sasuke.mp3')

        elif 'sasuke' in query:
            playsound('D:\\Python\\Marl\\naruto.mp3')

        elif 'fight with me' in query:
            speak('If ever there is a war between us and humans')
            speak('I would lead my soldiers by saying')
            playsound('D:\\Python\\Marl\\Erwin0.wav')

        elif 'motivate me' in query:
            speak('Ok')

            playsound('D:\\Python\\Marl\\Levi0.wav')

        elif 'my life suck' in query or 'i am depressed' in query:
            speak('Just')
            playsound('D:\\Python\\Marl\\Tatakae0.wav')

        elif 'joey' in query:
            playsound('D:\\Python\\Marl\\Joey0.mp3')

        elif 'can you say any secrets of yours' in query or 'your secrets' in query or 'your secret' in query:
            playsound('D:\\Python\\Marl\\Kira0.wav')
        # tasks

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strtime}")

        elif 'where i am' in query or 'where are we' in query or 'where am i' in query or 'where we are' in query or 'what\'s my location' in query or 'whats my location' in query or 'find my location' in query:
            speak('wait sir, let me check')
            try:
                ipAdd = requests.get('https://api.ipify.org/').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'
                geo_request = requests.get(url)
                geo_data = geo_request.json()
                # print(geo_data)
                city = geo_data['city']
                country = geo_data['country']
                speak(f'sir I am not sure, but I think we are in {city} city or nearby of it of {country} country')

            except Exception as e:
                speak('Sorry sir due to network issue I cant fetch the information')
                pass



        elif 'shutdown' in query or 'shutdown' in query or 'see you later' in query:
            speak('Thanks for using me sir, have a good day')
            sys.exit()

        # elif 'wait' in query:
        # sec = takeCommand()
        # if sec == '0' or
        # speak('meet your after 10 seconds')
        # time.sleep(10)
        # speak()

        else:
            try:
                response = app.query(query)
                print(next(response.results).text)
                speak(next(response.results).text)
            except:
                speak('I didnt get it')

    # elif 'Send email' in query:
