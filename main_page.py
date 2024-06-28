from email import message
from subprocess import call
from tkinter import *
from time import strftime
import datetime
from tracemalloc import stop
import speech_recognition as sr
import pyttsx3
import os
import webbrowser

class first():
    def __init__(self):

# --------------------------------------------  Code for virtual assistance  ----------------------------------------------------------------

        def Vir_Ass():
                # setting voice assistance
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

                    if __name__ == "__main__":

                        # wishme()
                        speak('Say something?')
                        try :
                            query = takecommand().lower()
                            if 'open youtube' in query:
                                    # webbrowser.open("youtube.com")
                                    speak('What do you want to search on youtube')
                                    a = takecommand().lower()
                                    if 'nothing' in query:
                                        speak("Okay ! ")
                                    else:
                                        speak('searching and openinig')
                                        webbrowser.open(f"https://www.youtube.com/results?search_query={a}")

                            elif 'open google' in query:
                                # webbrowser.open("www.google.com")
                                speak('What do you want to search on google')
                                b = takecommand().lower()
                                if 'nothing' in b:
                                    speak("Okay ! ")
                                else :
                                    speak('searching and openinig')
                                    webbrowser.open(f"https://www.google.com/search?q={b}")

                            elif "wikipedia" in query:
                                speak('What do you want to search on wikipedia')
                                a = takecommand().lower()
                                speak(f"Here what i found in wikipedia for {a}")
                                webbrowser.open(f"https://en.wikipedia.org/wiki/{a}")

                            elif "photoshop" in query:
                                os.startfile("C:\\Program Files\\Adobe\\Adobe Photoshop 2021\\Photoshop.exe")
                                # os.startfile('C:\\Users\\varun\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code.exe')
                            
                            elif 'time' in query:
                                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                                print(strTime)
                                speak(f"The time is{strTime}")

                            elif 'stop' in query:
                                pass

                            # elif 'quit' or 'exit' in query:
                                    # exit()

                            # elif "chrome" in query:
                            #     os.system('chrome')

                            elif "open calculator" in query:
                                call(["python","calculatorr.py"])

                            elif "open browser" or "browser" in query:
                                call(["python","brower.py"])
                                stop

                            elif "open QR code" or "QR code generator" in query:
                                call(["python","QR_code_generator.py"])


                            # elif " " in query:
                                # speak('Sorry! i didn''t get that')
                            print("Over")
                        
                        except Exception :
                            pass

# ----------------------------------------------------------------------------------------------------------------------------------------------


# -------------------------------------------------  FUNCTIONS  ----------------------------------------------------------------------------------

        # To display time which is at right bottom
        def time():
            st = strftime("%H:%M:%S %p")
            time_label.config(text=st)
            time_label.after(1000,time)

        # use when button About us is clicked 
        def about(event):
            abo = Toplevel(win)
            abo.title('About Us')
            abo.geometry('400x400')
            abo.config(bg='cyan')

            Txt1 = '''Application Hub is GUI application where different useful apps and games are organized and managed effectively and efficientlyover there. 
In this application you can access different useful apps and games in one platform ,you can also do it by voice commands 
which is one of its feature. 
This application is made to make the process of finding, managing and organizing apps easy and reliable.
This system is designed for every individual user . In this system multiple users can have access to their'''

            m = Message(abo,text=Txt1,font="Arial 12 bold",bg="cyan")
            m.place(x=5,y=30)

            abo.mainloop() 

        # used when button help me is clicked
        def help(event):
            hel = Toplevel(win)
            hel.title('Help')
            hel.geometry('400x400')
            hel.config(bg='cyan')

            Txt2 = '''
                --- Contact us ---

Email :- Applicationhub@gmail.com

Mob :- 9898292956

Website :- www.applicationhub.com'''

            m = Message(hel,text=Txt2,font="Arial 15 bold",bg="cyan")
            m.place(x=5,y=30)



            hel.mainloop() 


        # QR code scanner app
        def qr():
            call(["python","QR_code_generator.py"])


        # Mob Info Finder app code
        def mob_finder():
            call(["python","mob_num_finder.py"])


        # Browser app code
        def brow():
            call(["python","brower.py"])


        # Code for speed tester
        def speed():
            call(["python","speed_tester.py"])


        # Code for calculator
        def cal():
            call(["python","calculatorr.py"])


        # Code for motion detector
        def motion1():
            call(["python","Motion_detector.py"])


        # Code for To-do list
        def todo():
            call(["python","to-do-list.py"])


        # Flappy bird game code
        def flappy():
            call(["python","flappy_bird.py"])


        # Code for tic tac toe game
        def tic():
            call(["python","tictactoe.py"])


        # COde for pong game
        def poong():
            call(["python","pong.py"])


        # Code for snake game
        def snakee():
            call(["python","snake.py"])


        # Code for connect game
        def connect_game() :
            call(["python","coonect.py"])


# -------------------------------------------------  Creation class of window  ------------------------------------------------------------------

        class window(Tk):

            def __init__(self) :
                super().__init__()
                self.title("Application Hub")
                self.iconbitmap('APP_LOGO.ico')
                self.geometry(f'{1440}x{780}+{50}+{0}')
                self.resizable(False,False)

            def button(self,text,img,width,height,activebackground,activeforeground,font,bd,cmd,x,y):
                Button(text=text,image=img,width=width,height=height,cursor='hand2',activebackground=activebackground,
                activeforeground=activeforeground,font=font,bd=bd,relief=SOLID,command=cmd).place(x=x,y=y)
                
            def label(self,text,img,bg,fg,font,width,height,bd,anchor,x,y):
                Label(text=text,image=img,bg=bg,fg=fg,font=font,width=width,height=height,bd=bd,anchor=anchor).place(x=x,y=y)

#  -----------------------------------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------  Creating object of window class  ----------------------------------------------------------------

        win = window()
        win.config(bg='lightgrey')
        img4 = PhotoImage(file="bg1.png")
        lab2 = Label(win,image=img4)
        lab2.place(x=0,y=0)

# ------------------------------------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------  Frame 1  ----------------------------------------------------------------------------------------

        frame1 = Frame(win,highlightbackground='#404040',highlightthickness=5,width=1440,height=100,bg='#404040')
        frame1.place(x=0,y=0)

        label1 = Label(frame1,text="APPLICATION HUB",fg="#ffd700",font=('times new roman', 50 ,'bold'),bg='#404040')
        label1.place(x=50,y=0)

        img1 = PhotoImage(file="microphone64.png")
        mic_btn = Button(frame1,image=img1,cursor='hand2',bd=2,relief='solid',command=Vir_Ass)
        mic_btn.place(x=1340,y=11)

# ------------------------------------------------------------------------------------------------------------------------------------------------


# ------------------------------------------  Frame 2  -------------------------------------------------------------------------------------------
        
        # img2 = PhotoImage(file="app_bg.jpg")
        frame2 = Frame(win,highlightbackground='#404040',highlightthickness=2,width=796,height=550,bg='cyan')
        frame2.place(x=50,y=150)

        img5 = PhotoImage(file="bg2.png")
        lab2 = Label(frame2,image=img5)
        lab2.place(x=0,y=0)

        App_lab = Label(frame2,text="APPS",font=('Consolas 20 bold'),bg='#404040',fg='#ffd700',height=2,width=53)
        App_lab.place(x=0,y=0)

        # Button for App - 1
        img3 = PhotoImage(file="QR Code.png") 
        A1 = Button(frame2,image=img3,cursor='hand2',command=qr,bd=0)
        A1.place(x=80,y=100)

        # Button for App - 2
        img66 = PhotoImage(file="mmm.png") 
        A2 = Button(frame2,image=img66,cursor='hand2',command=mob_finder,bd=0)
        A2.place(x=330,y=100)

        # Button for App - 3 
        img7 = PhotoImage(file="Browser.png")
        A3 = Button(frame2,image=img7,bd=0,command=brow,cursor='hand2')
        A3.place(x=570,y=100)

        # Button for App - 4
        img8 = PhotoImage(file="Speed.png")
        A4 = Button(frame2,image=img8,bd=0,command=speed,cursor='hand2')
        A4.place(x=80,y=250)

        # Button for App - 5
        img9 = PhotoImage(file="Calculator (2).png")
        A5 = Button(frame2,image=img9,bd=0,command=cal,cursor='hand2')
        A5.place(x=330,y=250)
        
        # Button for App - 6
        img10 = PhotoImage(file="moton.png")
        A6 = Button(frame2,image=img10,bd=0,command=motion1,cursor='hand2')
        A6.place(x=570,y=250)

        # Button for App - 7
        img11 = PhotoImage(file="todo.png")
        A7 = Button(frame2,image=img11,bd=0,command=todo,cursor='hand2')
        A7.place(x=80,y=400)

# -------------------------------------------------------------------------------------------------------------------------------------------------



# -----------------------------------------------  Frame 3  --------------------------------------------------------------------------------------
        
        frame3 = Frame(win,highlightbackground='#404040',highlightthickness=2,bg='cyan')
        frame3.place(x=900,y=150,width=495,height=550)

        img6 = PhotoImage(file="bg2.png")
        lab2 = Label(frame3,image=img6)
        lab2.place(x=0,y=0)

        Game_lab = Label(frame3,text="GAMES",font=('Consolas 20 bold'),bg='#404040',fg='#ffd700',height=2,width=33)
        Game_lab.place(x=0,y=0)

        # Button for Game - 1
        img12 = PhotoImage(file="FB.png")
        G1 = Button(frame3,image=img12,bd=0,command=flappy,cursor='hand2')
        G1.place(x=150,y=100)

        # Button for Game - 2
        img13 = PhotoImage(file="tic.png")
        G2 = Button(frame3,image=img13,bd=0,command=tic,cursor='hand2')
        G2.place(x=150,y=190)

        # Button for Game - 3
        img14 = PhotoImage(file="conn.png")
        G3 = Button(frame3,image=img14,bd=0,command=connect_game,cursor='hand2')
        G3.place(x=150,y=280)

        # Button for Game - 4
        img15 = PhotoImage(file="snake.png")
        G4 = Button(frame3,image=img15,bd=0,command=snakee,cursor='hand2')
        G4.place(x=150,y=370)

        # Button for Game - 5
        img16 = PhotoImage(file="pong.png")
        G5 = Button(frame3,image=img16,bd=0,command=poong,cursor='hand2')
        G5.place(x=150,y=460)

# ------------------------------------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------   Last section  ---------------------------------------------------------------------------
        
        # This label will set grey background at bottom

        label3 = Label(win,bg='#404040',width=210,height=3)
        label3.place(x=0,y=735)

        # About button will display information about application
        About_btn = Button(win,text="About Us",underline=True,fg="#ffd700",bd=0,bg='#404040',font=('Consolas 15 bold'),cursor='hand2')
        About_btn.bind('<Button-1>',about)
        About_btn.place(x=600,y=740)

        # Sepeartor between about us and help button
        Labe4 = Label(win,bg='#404040',text="|",font=('Consolas 20 bold'),fg="#ffd700")
        Labe4.place(x=700,y=738)

        # This will open help page if required by user
        Help_btn = Button(win,text="Help",underline=True,fg="#ffd700",bd=0,bg='#404040',font=('Consolas 15 bold'),cursor='hand2')
        Help_btn.bind('<Button-1>',help)
        Help_btn.place(x=720,y=740)
        
        time_label = Label(win,font=(False,25,'bold'),bg='#404040',fg="#ffd700")
        time_label.place(x=1220,y=737)
        time()

# -----------------------------------------------------------------------------------------------------------------------------------------------

        # Termination of main window
        win.mainloop()


if __name__ == "__main__":
    a = first()