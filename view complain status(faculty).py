import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from subprocess import call

win=Tk()
win.geometry("900x600")
win.config(bg="pink")

def Back():
    win.destroy()
    call(["python","Faculty operation.py"])


l1=Label(win,text="MENTOR SYSTEM",fg="black",bg="lightgreen",font=("calibri",20,"bold"),padx=150,pady=10)
l1.grid(row=0,column=0,columnspan=20)
l1=Label(win,text="Guidance For Students",fg="black",bg='yellow',font=("calibri",18,"bold"),padx=100,pady=10)
l1.grid(row=1,column=0,columnspan=20)
l1=Label(win,text="VIEW COMPLAIN STATUS",fg="red",bg='pink',font=("calibri",17,"bold"),padx=50,pady=10)
l1.grid(row=2,column=0,columnspan=20)
l1=Label(win,text="Student id",bg='pink',font=("calibri",14),padx=10,pady=10)
l1.grid(row=3,column=0)
l1=Label(win,text="Full Name",bg='pink',font=("calibri",14),padx=10,pady=10)
l1.grid(row=3,column=1)
l1=Label(win,text="Roll no",bg='pink',font=("calibri",14),padx=10,pady=10)
l1.grid(row=3,column=2)
l1=Label(win,text="Complain id",bg='pink',font=("calibri",14),padx=10,pady=10)
l1.grid(row=3,column=3)
l1=Label(win,text="Complain type",bg='pink',font=("calibri",14),padx=10,pady=10)
l1.grid(row=3,column=4)
l1=Label(win,text="Complain Details",bg='pink',font=("calibri",14),padx=10,pady=10)
l1.grid(row=3,column=5)
l1=Label(win,text="Complain Status",bg='pink',font=("calibri",14),padx=10,pady=10)
l1.grid(row=3,column=6)

conn=mysql.connector.connect(host="localhost",username="root",password="deepika21",database="world")
cursor=conn.cursor()
cursor.execute("SELECT * from complainregform")
r=cursor.fetchall()
num=5
for i in r:
        Student_id=Label(win,text=i[0],fg='blue',bg='pink',font=("calibri",12)).grid(row=num,column=0,padx=10,pady=10)
        Full_Name=Label(win,text=i[1],fg='blue',bg='pink',font=("calibri",12)).grid(row=num,column=1,padx=10,pady=10)
        Roll_no=Label(win,text=i[2],fg='blue',bg='pink',font=("calibri",12)).grid(row=num,column=2,padx=10,pady=10)
        Complain_id=Label(win,text=i[3],fg='blue',bg='pink',font=("calibri",12)).grid(row=num,column=3,padx=10,pady=10)
        Complain_type=Label(win,text=i[4],fg='blue',bg='pink',font=("calibri",12)).grid(row=num,column=4,padx=10,pady=10)
        Complain_Details=Label(win,text=i[5],fg='blue',bg='pink',font=("calibri",12)).grid(row=num,column=5,padx=10,pady=10)
        Complain_Status=Label(win,text=i[6],fg='blue',bg='pink',font=("calibri",12)).grid(row=num,column=6,padx=10,pady=10)


       
        conn.commit()
        num=num+1
conn.close()

b1=Button(win,text="<==",command=Back,bg='red',fg='white',bd=4)
b1.place(x=850,y=550)

win.mainloop()
