from tkinter import*
from subprocess import call
from tkinter import messagebox as mb
# import mysql.connector

win=Tk()
win.geometry("600x300")

img=PhotoImage(file="bg.png")
img_label=Label(win,image=img)
img_label.place(x=0,y=0)

logo=PhotoImage(file="python_logo.png")
logo_label=Label(win,image=logo)
logo_label.grid(padx=100,pady=150)



def Admin():
    win.destroy()
    call(["pyw","adminlogin.py"])
def Student():
    win.destroy()
    call(["pyw","studentlogin.py"])
def Principal():
    win.destroy()
    call(["pyw","principallogin.py"])
def Faculty():
    win.destroy()
    call(["pyw","facultylogin.py"])    

    

l1=Label(win,text="MENTOR SYSTEM",fg="black",bg="lightgreen",font=("calibri",20,"bold"))
l1.place(x=150,y=20)
l2=Label(win,text="GUIDANCE FOR STUDENTS",fg="black",font=("calibri",15,"bold"))
l2.place(x=140,y=60)

b1=Button(win,text="ADMIN",fg="black",bg="pink",command=Admin,font=("calibri",15,"bold"))
b1.place(x=50,y=100)
b2=Button(win,text="STUDENT",fg="black",bg="pink",command=Student,font=("calibri",15,"bold"))
b2.place(x=150,y=100)  
b3=Button(win,text="PRINCIPAL",fg="black",bg="pink",command=Principal,font=("calibri",15,"bold"))
b3.place(x=260,y=100)
b4=Button(win,text="FACULTY",fg="black",bg="pink",command=Faculty,font=("calibri",15,"bold"))
b4.place(x=380,y=100)

l3=Label(win,text="DEVELOPED BY:",fg="black",bg="light blue",font=("calibri",15,"bold"))
l3.place(x=400,y=160)
l4=Label(win,text="Sarthak Dash",fg="black",bg="light yellow",font=("calibri",10,"bold"))
l4.place(x=400,y=192)
l5=Label(win,text="Monalisa Pal",fg="black",bg="light yellow",font=("calibri",10,"bold"))
l5.place(x=400,y=215)
l6=Label(win,text="Deepika Sahoo",fg="black",bg="light yellow",font=("calibri",10,"bold"))
l6.place(x=400,y=240)
l7=Label(win,text="PYTHON PROJECT",fg="black",bg="light blue",font=("calibri",20,"bold"))
l7.place(x=50,y=210)


win.mainloop()         
             
