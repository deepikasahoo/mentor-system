from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from subprocess import call
import mysql.connector

win=Tk()
win.geometry("1200x600")


def Back():
    win.destroy()
    call(["pyw","Admin operation.py"])


l1=Label(win,text="MENTOR SYSTEM",fg="black",bg="lightgreen",font=("calibri",20,"bold"),padx=150,pady=10)
l1.grid(row=0,column=0,columnspan=20)
l1=Label(win,text="Guidance For Students",fg="black",bg='yellow',font=("calibri",18,"bold"),padx=100,pady=10)
l1.grid(row=1,column=0,columnspan=20)
l1=Label(win,text="VIEW STUDENTS INFORMATION",fg="red",bg='pink',font=("calibri",17,"bold"),padx=50,pady=10)
l1.grid(row=2,column=0,columnspan=20)
l1=Label(win,text="Student id",fg='black',font=("calibri",15),padx=10,pady=10)
l1.grid(row=3,column=0)
l1=Label(win,text="Full Name",fg='black',font=("calibri",15),padx=10,pady=10)
l1.grid(row=3,column=1)
l1=Label(win,text="Userid",fg='black',font=("calibri",15),padx=10,pady=10)
l1.grid(row=3,column=2)
l1=Label(win,text="Password",fg='black',font=("calibri",15),padx=10,pady=10)
l1.grid(row=3,column=3)
l1=Label(win,text="RollNo",fg='black',font=("calibri",15),padx=10,pady=10)
l1.grid(row=3,column=4)
l1=Label(win,text="MobileNo",fg='black',font=("calibri",15),padx=10,pady=10)
l1.grid(row=3,column=5)
l1=Label(win,text="Emailid",fg='black',font=("calibri",15),padx=10,pady=10)
l1.grid(row=3,column=6)
l1=Label(win,text="AdhaarNo",fg='black',font=("calibri",15),padx=10,pady=10)
l1.grid(row=3,column=7)
l1=Label(win,text="BloodGroup",fg='black',font=("calibri",15),padx=10,pady=10)
l1.grid(row=3,column=8)
l1=Label(win,text="Gender",fg='black',font=("calibri",15),padx=10,pady=10)
l1.grid(row=3,column=9)
l1=Label(win,text="State",fg='black',font=("calibri",15),padx=10,pady=10)
l1.grid(row=3,column=10)

conn=mysql.connector.connect(host="localhost",username="root",password="deepika21",database="world")
cursor=conn.cursor()
cursor.execute("Select * from stdregdform")
r=cursor.fetchall()
num=5
for i in r:
        Student_id=Label(win,text=i[0],fg='blue',bg='pink',font=("calibri",12)).grid(row=num,column=0,padx=10,pady=10)
        Full_Name=Label(win,text=i[1],fg='blue',bg='white',font=("calibri",12)).grid(row=num,column=1,padx=10,pady=10)
        Userid=Label(win,text=i[2],fg='blue',bg='white',font=("calibri",12)).grid(row=num,column=2,padx=10,pady=10)
        Password=Label(win,text=i[3],fg='blue',bg='white',font=("calibri",12)).grid(row=num,column=3,padx=10,pady=10)
        RollNo=Label(win,text=i[4],fg='blue',bg='white',font=("calibri",12)).grid(row=num,column=4,padx=10,pady=10)
        MobileNo=Label(win,text=i[5],fg='blue',bg='white',font=("calibri",12)).grid(row=num,column=5,padx=10,pady=10)
        Emailid=Label(win,text=i[6],fg='blue',bg='white',font=("calibri",12)).grid(row=num,column=6,padx=10,pady=10)
        AdhaarNo=Label(win,text=i[7],fg='blue',bg='white',font=("calibri",12)).grid(row=num,column=7,padx=10,pady=10)
        BloodGroup=Label(win,text=i[8],fg='blue',bg='white',font=("calibri",12)).grid(row=num,column=8,padx=10,pady=10)
        Gender=Label(win,text=i[9],fg='blue',bg='white',font=("calibri",12)).grid(row=num,column=9,padx=10,pady=10)
        State=Label(win,text=i[10],fg='blue',bg='white',font=("calibri",12)).grid(row=num,column=10,padx=10,pady=10)
        conn.commit()
        num=num+1
conn.close()

b1=Button(win,text="<==",command=Back,bg='red',fg='black',bd=4)
b1.place(x=1150,y=550)

win.mainloop()

