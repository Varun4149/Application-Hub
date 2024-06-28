from tkinter import *
import speech_recognition as sr
import pyttsx3
import datetime
import os
import webbrowser
import wikipedia


# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()

#     # Enable low security in gmail
#     server.login('your email id', 'your email password')
#     server.sendmail('your email id', to, content)
#     server.close()

# setting voice assistance
class vir():
    def __init__(self):
        engine =  pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice',voices[2].id)
        def speak(audio):
            engine.say(audio)
            engine.runAndWait()

        def takecommand():
            r = sr.Recognizer()
            with sr.Microphone()  as source:
                print("Listening..")
                r.pause_threshold = 1
                audio = r.listen(source)
            try :
                print("Recognizing....")
                qurey = r.recognize_google(audio,language='en-in' )
                print(f"user said: {qurey}\n")
            except Exception :
                # print("say that again please....")
                speak("Sorry! I cant hear you, can you speak loud")
                takecommand()
                # return "None"
            return qurey

        def wishme():
            hour = int(datetime.datetime.now().hour)
            if hour>=0 and hour<12:
                speak("Good Morning")
            elif hour >=10 and hour<18:
                speak("Good afternon")
            else :
                speak("Good evening")
            speak("I am Jarvis sir. please tell me how may I help you")


            # wishme()
            speak('Say something?')
            try :
                query = takecommand().lower()
                if 'open youtube' in query:
                        # webbrowser.open("youtube.com")
                        speak('What do you want to search on youtube')
                        a = takecommand().lower()
                        if 'nothing' in a:
                            speak("Okay !")
                        else:
                            speak('searching and openinig')
                            webbrowser.open(f"https://www.youtube.com/results?search_query={a}")

                elif 'open google' in query:
                    # webbrowser.open("www.google.com")
                    speak('What do you want to search on google')
                    b = takecommand().lower()
                    if 'nothing' in b:
                        speak("Okay !")
                    else :
                        speak('searching and openinig')
                        webbrowser.open(f"https://www.google.com/search?q={b}")

                # elif "wikipedia" in query:
                #     speak('What do you want to search on wikipedia')
                #     a = takecommand().lower()
                #     speak(f"Here what i found in wikipedia for {a}")
                #     webbrowser.open(f"https://en.wikipedia.org/wiki/{a}")

                elif 'wikipedia' in query:
                    # if any one wants to have a information
                    # from wikipedia
                    speak("Checking the wikipedia ")
                    query = query.replace("wikipedia", "")
                    # it will give the summary of 4 lines from 
                    # wikipedia we can increase and decrease 
                    # it also.
                    result = wikipedia.summary(query, sentences=4)
                    speak("According to wikipedia")
                    speak(result)

                elif "photoshop" in query:
                    os.startfile("C:\\Program Files\\Adobe\\Adobe Photoshop 2021\\Photoshop.exe")
                    # os.startfile('C:\\Users\\varun\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code.exe')

                elif 'time' in query:
                    strTime = datetime.datetime.now().strftime("%H" +" Hours"+":%M"+" Minutes"+":%S"+" Seconds")
                    print(strTime)
                    speak(f"The time is {strTime}")

                elif "day" in query:
                    day = datetime.datetime.today().weekday() + 1
                    Day_dict = {1: 'Monday', 2: 'Tuesday', 
                                3: 'Wednesday', 4: 'Thursday', 
                                5: 'Friday', 6: 'Saturday',
                                7: 'Sunday'}
                    if day in Day_dict.keys():
                        day_of_the_week = Day_dict[day]
                        print(day_of_the_week)
                        speak("The day is " + day_of_the_week)

                elif 'stop' in query:
                    pass
                
                elif 'quit' or 'exit' in query:
                        exit()

                elif "chrome" in query:
                    os.system('chrome')

                else :
                    speak('Sorry! i didn''t get that')

                print("Over")
            except Exception :
                pass

if __name__ == "__main__" :
    vir()