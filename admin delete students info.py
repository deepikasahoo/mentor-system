from tkinter import*
from tkinter import ttk
from tkinter import messagebox as mb
from subprocess import call
import mysql.connector

win=Tk()
win.geometry("600x600")
win.config(bg="#B2A59B")

l1=Label(win,text="MENTOR SYSTEM",fg="black",bg="light green",font=("calibri",25,"bold"))
l1.place(x=150,y=50)
l2=Label(win,text="GUIDANCE FOR STUDENTS",fg="black",bg="pink",font=("calibri",20,"bold"))
l2.place(x=120,y=100)
l3=Label(win,text="CHANGE PASSWORD(ADMIN)",fg="black",bg="#B2A59B",font=("calibri",18,"bold"))
l3.place(x=120,y=140)

l4=Label(win,text="Current Password:",fg="black",bg="#B2A59B",font=("calibri",20,"bold"))
l4.place(x=60,y=200)
t1=Entry(win,fg="black",bg="white",font=("calibri",15,"bold"))
t1.place(x=280,y=205)
l5=Label(win,text="New Password:",fg="black",bg="#B2A59B",font=("calibri",20,"bold"))
l5.place(x=60,y=250)
t2=Entry(win,fg="black",bg="white",font=("calibri",15,"bold"))
t2.place(x=280,y=255)

b1=Button(win,text="SAVE",fg="black",bg="light yellow",font=("calibri",15,"bold"))
b1.place(x=200,y=350)
b2=Button(win,text="CANCEL",fg="black",bg="light yellow",font=("calibri",15,"bold"))
b2.place(x=280,y=350)
b3=Button(win,text="<==",fg="black",bg="red",font=("calibri",15,"bold"))
b3.place(x=470,y=480)

win.mainloop()         
