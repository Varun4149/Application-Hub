from logging import root
import re
from tkinter import*
import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage

class qrc() :
    def __init__(self) :

        class Qr_Generator:
            def __init__(self,root):
                self.root=root
                self.root.geometry("950x600+200+50")
                self.root.title("QR Generator")
                self.root.resizable(False,False)

                title=Label(self.root,text="   QR Code Generator",font=("times new roman",40),bg='#053246',fg='white',anchor='w').place(x=0,y=0,relwidth=1)

                #====Student Details window=========
                #===Variables=====
                self.var_emp_code=StringVar()
                

                emp_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
                emp_Frame.place(x=50,y=100,width=520,height=480)

                emp_title=Label(emp_Frame,text="Qr Code Generator",font=("goudy old style",20),bg='#043256',fg='white').place(x=0,y=0,relwidth=1)

                lbl_emp_code=Label(emp_Frame,text="Enter URL:",font=("times new roman",14,'bold'),bg='white').place(x=200,y=120)
                
                
                txt_emp_code=Entry(emp_Frame,font=("times new roman",14),textvariable=self.var_emp_code,bg='lightyellow').place(x=80,y=160,width=350,height=80)
            

                btn_generate=Button(emp_Frame,text='QR Generate',command=self.generate,font=("times new roman",17,'bold'),bg='#2196f3',fg='white').place(x=60,y=320,width=200,height=50)
                btn_clear=Button(emp_Frame,text='Clear',command=self.clear,font=("times new roman",17,'bold'),bg='#607d8b',fg='white').place(x=290,y=320,width=140,height=50)
                
                self.msg=''
                self.lbl_msg=Label(emp_Frame,text=self.msg,font=("times new roman",19),bg='white',fg='green')
                self.lbl_msg.place(x=0,y=405,relwidth=1)

                #====Student QR Code window=========
                qr_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
                qr_Frame.place(x=620,y=100,width=290,height=480)

                emp_title=Label(qr_Frame,text="QR Code",font=("goudy old style",20),bg='#043256',fg='white').place(x=0,y=0,relwidth=1)

                self.qr_code=Label(qr_Frame,text='No QR\nAvailable',font=('times new roman',15),bg='#3f51b5',fg='white',bd=1,relief=RIDGE)
                self.qr_code.place(x=35,y=85,width=220,height=200)

            def clear(self):
                self.var_emp_code.set('')
                
                self.msg=''
                self.lbl_msg.config(text=self.msg)
                self.qr_code.config(image='')
                
            def generate(self):
                if self.var_emp_code.get()=='':
                    self.msg='All Fields are Required!!!'
                    self.lbl_msg.config(text=self.msg,fg='red')
                else:
                    qr_data=(f"Click Here: {self.var_emp_code.get()}")
                    qr_code=qrcode.make(qr_data)
                    print(qr_code)
                    qr_code=resizeimage.resize_cover(qr_code,[180,180])
                    
                    
                    qr_code.save("C:\\Users\\varun\\OneDrive\\Desktop\\Python\\Projects\\Student_QR/QR Code "+'.png')
                    
                    
                    #=======QR Code Image Update===========
                    self.im=ImageTk.PhotoImage(file="C:\\Users\\varun\\OneDrive\\Desktop\\Python\\Projects\\Student_QR/QR Code "+'.png')
                    
                    self.qr_code.config(image=self.im)
                    #=======updating Notification==========
                    self.msg='QR Generated Successfully!!!'
                    self.lbl_msg.config(text=self.msg,fg='green')


        root=Tk()
        obj =Qr_Generator(root)
        root.mainloop()

if __name__ == "__main__":
    qrc()