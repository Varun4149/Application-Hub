from tkinter.font import BOLD

import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from tkinter import * 
from tkinter import ttk


def mob_get():
    a = mob.get()
    print(a)

    number = f"+91 {a}"

    ch_num = phonenumbers.parse(number,"CH")
    x = geocoder.description_for_number(ch_num,"en")

    service_num = phonenumbers.parse(number,"CH")
    y = carrier.name_for_number(service_num,"en")

    b = f"Mobile details :- \n{x}\n{y}"
    mob_info = Message(win,text=b,font=("times new roman",20,BOLD),width=300,bg="lightgreen")
    mob_info.place(x=30,y=230)


win = Tk()
win.config(bg="lightgreen")

win.title("Mobile info finder")
win.geometry(f'{400}x{400}+{600}+{200}')

mob_no = Label(win,text="Enter Mobile Num ",font=("times new roman",30,BOLD),bg="lightgreen",fg="coral")
mob_no.place(x=32,y=30)

mob = StringVar()
mob_in = ttk.Entry(win,textvariable=mob,font=("times new roman",25,BOLD))
mob_in.place(x=30,y=100)

btn = Button(win,text="Enter",font=("times new roman",20,BOLD),command=mob_get,bg="white",fg="blue")
btn.place(x=140,y=170)

# number = "+91 9850994149"

# ch_num = phonenumbers.parse(number,"CH")
# print(geocoder.description_for_number(ch_num,"en"))

# service_num = phonenumbers.parse(number,"CH")
# print(carrier.name_for_number(service_num,"en"))


win.mainloop()