from subprocess import call
from tkinter import ttk
from tkinter.ttk import Progressbar
from tkinter import *


w=Tk()

width_of_window = 427
height_of_window = 250
screen_width = w.winfo_screenwidth() 
screen_height = w.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
w.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))

w.overrideredirect(1)
a='#249794'


s = ttk.Style()
s.theme_use('clam')
s.configure("red.Horizontal.TProgressbar", foreground='red', background='#4f4f4f')
progress=Progressbar(w,style="red.Horizontal.TProgressbar",orient=HORIZONTAL,length=500,mode='determinate',)

#############progressbar          33333333333333333333333333333
def new_win():
        call(["python","Login_page.py"])


def bar():

    l4=Label(w,text='Loading...',fg='white',bg=a)
    lst4=('Calibri (Body)',15)
    l4.config(font=lst4)
    l4.place(x=18,y=210)
    
    import time
    r=0
    for i in range(100):
        progress['value']=r
        w.update_idletasks()
        time.sleep(0.01)
        r=r+1
    
    w.destroy()
    new_win()

        

progress.place(x=-10,y=235)


Frame(w,width=427,height=241,bg=a,highlightbackground='black',highlightthickness=1).place(x=0,y=0) 

la = Label(w,width=60,bg='#4f4f4f')
la.place(x=0,y=0)

b1=Button(w,width=20,height=1,text='Get Started',command=bar,border=0,fg=a,bg='white',cursor='hand2')
b1.place(x=140,y=200)

######## Label

l1=Label(w,text='APPLICATION',fg='white',bg=a,underline=2)
lst1=('Calibri (Body)',25,'bold')
l1.config(font=lst1)
l1.place(x=30,y=70)

l2=Label(w,text='HUB',fg='white',bg=a)
lst2=('Calibri (Body)',20)
l2.config(font=lst2)
l2.place(x=255,y=75)

l3=Label(w,text='',fg='white',bg=a)
lst3=('Calibri (Body)',13)
l3.config(font=lst3)
l3.place(x=30,y=112)


w.mainloop()

