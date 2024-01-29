import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from subprocess import call

win=Tk()
win.geometry("600x600")
win.config(bg="pink")

def Back():
    win.destroy()
    call(["pyw","principal operation.py"])
def Close():
    win.destroy()
    call(["pyw","welcomepage.py"])


l1=Label(win,text="MENTOR SYSTEM",fg="black",bg="lightgreen",font=("calibri",20,"bold"),padx=100,pady=10)
l1.grid(row=0,column=0,columnspan=10)
l1=Label(win,text="Guidance For Students",fg="black",bg='yellow',font=("calibri",18,"bold"),padx=50,pady=10)
l1.grid(row=1,column=0,columnspan=20)
l1=Label(win,text="VIEW FEEDBACK",fg="red",bg='pink',font=("calibri",17,"bold"),padx=10,pady=10)
l1.grid(row=2,column=0,columnspan=20)
l1=Label(win,text="Student id",bg='pink',font=("calibri",14),padx=50,pady=10)
l1.grid(row=3,column=0)
l1=Label(win,text="Password",bg='pink',font=("calibri",14),padx=30,pady=10)
l1.grid(row=3,column=1)
l1=Label(win,text="Rate Your Feedback",bg='pink',font=("calibri",14),padx=50,pady=10)
l1.grid(row=3,column=2)

conn=mysql.connector.connect(host="localhost",username="root",password="deepika21",database="world")
cursor=conn.cursor()
cursor.execute("SELECT * from feedbackform")
r=cursor.fetchall()
num=5
for i in r:
        Student_id=Label(win,text=i[0],fg='blue',bg='pink',font=("calibri",12)).grid(row=num,column=0,padx=10,pady=10)
        Password=Label(win,text=i[1],fg='blue',bg='pink',font=("calibri",12)).grid(row=num,column=1,padx=10,pady=10)
        Rate_Your_Feedback=Label(win,text=i[2],fg='blue',bg='pink',font=("calibri",12)).grid(row=num,column=2,padx=10,pady=10)
        
       
        conn.commit()
        num=num+1
conn.close()

b1=Button(win,text="<==",command=Back,bg='red',fg='white',bd=4)
b1.place(x=550,y=520)
b1=Button(win,text="X",command=Close,bg='red',fg='white',bd=4)
b1.place(x=0,y=0)

win.mainloop()
