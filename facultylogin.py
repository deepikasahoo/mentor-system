from tkinter import*
from subprocess import call
from tkinter import messagebox as mb

win=Tk()
win.geometry("600x600")
def Back():
    win.destroy()
    call(["python","welcomepage.py"])
def registration():
    win.destroy()
    call(["python","registrationform.py"])    


l1=Label(win,text="MENTOR SYSTEM",fg="black",bg="lightgreen",font=("calibri",20,"bold"))
l1.place(x=150,y=20)

l2=Label(win,text="GUIDANCE FOR STUDETNS",fg="black",bg="pink",font=("calibri",15,"bold"))
l2.place(x=130,y=60)

l3=Label(win,text="FACULTY LOGIN",fg="black",bg="light yellow",font=("calibri",15,"bold"))
l3.place(x=170,y=95)

l4=Label(win,text="Username:",fg="black",font=("calibri",15,"bold"))
l4.place(x=50,y=150)

l5=Label(win,text="Password:",fg="black",font=("calibri",15,"bold"))
l5.place(x=50,y=200)

t1=Entry(win,fg="black",bg="white",font=("calibri",15,"bold"))
t1.place(x=150,y=150)
t2=Entry(win,fg="black",bg="white",font=("calibri",15,"bold"))
t2.place(x=150,y=200)

b1=Button(win,text="Login",fg="black",bg="light yellow",font=("calibri",15,"bold"))
b1.place(x=80,y=250)
b2=Button(win,text="Cancel",fg="black",bg="light yellow",font=("calibri",15,"bold"))
b2.place(x=160,y=250)
b3=Button(win,text="Reset",fg="black",bg="light yellow",font=("calibri",15,"bold"))
b3.place(x=250,y=250)
b4=Button(win,text="Registration",fg="black",command=registration,bg="light blue",font=("calibri",15,"bold"))
b4.place(x=160,y=350)


l5=Label(win,text="Are you a new user? if yes then click on Registration",fg="black",font=("calibri",12,"bold"))
l5.place(x=50,y=300)

b5=Button(win,text="<==",fg="black",command=Back,bg="Red",font=("calibri",15,"bold"))
b5.place(x=350,y=390)

win.mainloop()         


             

