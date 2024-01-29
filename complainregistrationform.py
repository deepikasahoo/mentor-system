from tkinter import*
from tkinter import ttk
from subprocess import call
import mysql.connector
from tkinter import messagebox as mb

win=Tk()
win.geometry("600x600")
'''win.config(bg="black")'''
def Back():
    win.destroy
    call("pyw","student operation.py")

l1=Label(win,text="MENTOR SYSTEM",fg="black",bg="lightgreen",font=("calibri",25,"bold"))
l1.place(x=150,y=20)
l2=Label(win,text="GUIDANCE FOR STUDENTS",fg="black",bg="pink",font=("calibri",15,"bold"))
l2.place(x=160,y=70)
l3=Label(win,text="COMPLAIN REGISTRATION FORM",fg="black",bg="#FFCF81",font=("calibri",15,"bold"))
l3.place(x=145,y=110)

l4=Label(win,text="Student id:",fg="black",font=("calibri",15,"bold"))
l4.place(x=80,y=180)
t1=Entry(win,fg="black",bg="white",font=("calibri",15,"bold"))
t1.place(x=230,y=180)

l5=Label(win,text="Password:",fg="black",font=("calibri",15,"bold"))
l5.place(x=80,y=220)
t2=Entry(win,fg="black",bg="white",font=("calibri",15,"bold"))
t2.place(x=230,y=220)

Complian_type=Label(win,text="Complian type",font=("calibri",15,"bold"))
Complian_type.place(x=80,y=260)

compliain_list=ttk.Combobox(win,values=["Books","Uniforms","Library","Teacher","Education","Hostel"])
compliain_list["state"]="readonly"
compliain_list.set("--Select--")
compliain_list.place(x=230,y=265)

Complain_details=Label(win,text="Complain details",font=("calibri",15,"bold"))
Complain_details.place(x=80,y=300)
Complain_details=Entry(win,fg="black",bg="white",font=("calibri",15,"bold"))
Complain_details.place(x=230,y=300)

Submit=Button(win,text="SUBMIT",fg="black",bg="light blue",font=("calibri",15,"bold"))
Submit.place(x=200,y=350)
Cancel=Button(win,text="CANCEL",fg="black",bg="light blue",font=("calibri",15,"bold"))
Cancel.place(x=300,y=350)

Back=Button(win,text="<==",fg="black",bg="red",command=Back,font=("calibri",15,"bold"))
Back.place(x=500,y=450)


win.mainloop()
