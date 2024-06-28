# from ast import Call
from tkinter import messagebox
import mysql.connector
from subprocess import call
from time import strftime
from tkinter import *
from tkinter import ttk


class login:
    def __init__(self):

        def Ok():
            mysqldb= mysql.connector.connect(host="localhost", user="root", password="", database="test1")
            mycursor = mysqldb.cursor()
            # uname = b1.get()
            uname = user_txt.get()
            password = pass_txt.get()
            sql = "select * from Login where uname = %s and password= %s"
            mycursor.execute(sql, [(uname), (password)])
            results = mycursor.fetchall()
            if results:
                # messagebox.showinfo("","Login Success")
                # root.destroy()
                call(["python","main_page.py"])
                # win.destroy()     
                return True

            elif user_name.get() == "" or pass_name.get() == "":
                messagebox.showinfo("","Please enter text first")
            else :
                messagebox.showinfo("", "Incorrent Username and Password")
                return False


        win = Tk()
        win .title("Application Hub")
        win.iconbitmap('APP_LOGO.ico')
        win.geometry(f'{310}x{410}+{680}+{180}')
        win.resizable(False,False)
        win.config(bg="lightyellow",borderwidth=2)
        win.overrideredirect(1)

        login_lab = Label(win,text="Login",font=('Consolas 20 bold'),bg='#404040',fg='#ffd700',height=2,width=20)
        login_lab.place(x=0,y=0)

        user_id = Label(win,text="UserName : ",font=('times new roman', 15,'bold'),bg = "lightyellow")
        user_id.place(x=100,y=100)

        global user_txt
        user_txt = StringVar()
        user_name = ttk.Entry(win,textvariable=user_txt,width=20,font=('times new roman', 15,'bold'))
        user_name.place(x=50,y=150)

        global pass_txt
        pass_id = Label(win,text="Password : ",font=('times new roman', 15,'bold'),bg = "lightyellow")
        pass_id.place(x=100,y=200)

        pass_txt = StringVar()
        pass_name = ttk.Entry(win,show="*",textvariable=pass_txt,width=20,font=('times new roman', 15,'bold'))
        pass_name.place(x=50,y=250)

        login_btn = Button(win,text="login",width=10,font=('times new roman',12,'bold'),relief=RIDGE,border=1,bg='lightblue',cursor='hand2',command=Ok)
        login_btn.place(x=40,y=320)

        Exit_btn = Button(win,text="Exit",width=10,font=('times new roman',12,'bold'),relief=RIDGE,border=1,bg='lightblue',cursor='hand2',command=exit)
        Exit_btn.place(x=170,y=320)

        win.mainloop()


if __name__ == "__main__":
    login()
