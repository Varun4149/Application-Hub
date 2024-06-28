# Python program to test
# internet speed
from tkinter import *
from tkinter import messagebox
import speedtest

class hey():
    def __init__(self) :
        st = speedtest.Speedtest()

# option = int(input('''What speed do you want to test:

# 1) Download Speed

# 2) Upload Speed

# 3) Ping

# Your Choice: '''))


# if option == 1:

# 	print(st.download())

# elif option == 2:

# 	print(st.upload())

# elif option == 3:

# 	servernames =[]

# 	st.get_servers(servernames)

# 	print(st.results.ping)

# else:

# 	print("Please enter the correct choice !")

        win = Tk()
        win.title("NETSpeed")
        # win.iconbitmap('speedtesticon.ico')
        win.geometry('300x250')
        win.resizable(False,False)
        win.config(bg='magenta')
        win.eval('tk::PlaceWindow . Centre')

        def download():
            # a = (str(st.download())+" Bytes per second")
            x = int(st.download())
            y = int(x/1024/1024)
            a = (str(y)+ " Mbps")
            messagebox.showinfo("your download speed",a)

        def upl():
            x = int(st.upload())
            y = int(x/1024/1024)
            # b = (str(st.upload())+" Bytes per second")
            b = (str(y)+ " Mbps")
            messagebox.showinfo("your upload speed",b)

        def ping():
            servernames =[]
            st.get_servers(servernames)
            # print(st.results.ping)
            c = (str(st.results.ping))
            messagebox.showinfo("your upload speed",c)


        stext = StringVar()
        stext = 'Speed Tester'
        L1 = LabelFrame(win,text=stext,labelanchor='n' ,borderwidth=5,font=('Consolas 30 bold'),fg='black',bg='magenta',border=0)
        L1.pack(fill='both',expand='yes',padx=10,pady=10)


        B1 = Button(L1,text='Download Speed',font=('Consolas', 15 , 'bold'),command=download,bg='cyan',relief='solid')
        B1.pack(padx=10,pady=10)

        B2 = Button(L1,text='Upload Speed',font=('Consolas', 15 , 'bold'),command=upl,bg='cyan',relief='solid')
        B2.pack(padx=10,pady=10)

        B2 = Button(L1,text='Ping',font=('Consolas', 15 , 'bold'),command=ping,bg='cyan',relief='solid')
        B2.pack(padx=10,pady=10)

        win.mainloop()

if __name__ == "__main__":
    hey()