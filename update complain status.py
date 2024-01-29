from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox as mb

win=Tk()
win.geometry("500x500")

l1=Label(win,text="MENTOR SYSTEM",fg="black",bg="light green",font=("calibri",20,"bold"))
l1.place(x=150,y=20)
l2=Label(win,text="GUIDANCE FOE STUDENTS",fg="black",bg="pink",font=("calibri",15,"bold"))
l2.place(x=140,y=60)
l3=Label(win,text="UPDATE COMPLAIN STATUS",fg="blue",bg="light yellow",font=("calibri",15,"bold"))
l3.place(x=130,y=95)

complain_id=Label(win,text="Complain id:",fg="black",font=("calibri",15,"bold"))
complain_id.place(x=50,y=150)
t1=Entry(win,fg="black",font=("calibri",15,"bold"))
t1.place(x=185,y=150)
update_status=Label(win,text="Update status:",font=("calibri",15,"bold"))
update_status.place(x=50,y=200)
t2=Entry(win,fg="black",font=("calibri",15,"bold"))
t2.place(x=185,y=200)

var=IntVar()
rb1=Radiobutton(win,text="Pending",value=1,variable=var)
rb1.place(x=150,y=250)
rb2=Radiobutton(win,text="Close",value=2,variable=var)
rb2.place(x=220,y=250)

submit=Button(win,text="SUBMIT",fg="black",bg="light blue",font=("calibri",15,"bold"))
submit.place(x=130,y=290)
cancel=Button(win,text="CANCEL",fg="black",bg="light blue",font=("calibri",15,"bold"))
cancel.place(x=250,y=290)

Back=Button(win,text="<==",fg="black",bg="red",font="bold")
Back.place(x=390,y=360)
                                                                 






win.mainloop()
