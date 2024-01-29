from tkinter import*
from tkinter import messagebox as mb
from subprocess import call
import mysql.connector

win=Tk()
win.geometry("600x600")
def Back():
    win.destroy()
    call(["pyw","studentlogin.py"])

def Self_Update():
     win.destroy()
     call(["pyw","studentupdateform.py"])
     
def Raise_a_Complain():
     win.destroy()
     call(["pyw","raise_complain_status.py"])
    
def View_Complain_Status():
     win.destroy()
     call(["pyw","view complain status(student).py"])  

def Change_Password():
      win.destroy()
      call(["pyw","student changepassword.py"])

def Feedback():
      win.destroy()
      call(["pyw","studentfeedbackform.py"])

def Logout():
      win.destroy()
      call(["pyw","studentlogin.py"])

l1=Label(win,text="MENTOR SYSTEM",fg="black",bg="lightgreen",font=("calibri",25,"bold"))
l1.place(x=150,y=20)
l2=Label(win,text="Guidance For Students",fg="black",bg="pink",font=("calibri",15,"bold"))
l2.place(x=170,y=70)
l3=Label(win,text="Student Operation",fg="black",font=("calibri",15,"bold"))
l3.place(x=190,y=100)

b1=Button(win,text="Raise a  Complain",command=Raise_a_Complain,fg="black",bg="white",font=("calibri",15,"bold"))
b1.place(x=20,y=150)
b2=Button(win,text="Update",command=Self_Update,fg="black",bg="white",font=("calibri",15,"bold"))
b2.place(x=20,y=200)

b3=Button(win,text="View Complain Status",command=View_Complain_Status,fg="black",bg="white",font=("calibri",15,"bold"))
b3.place(x=20,y=250)
b4=Button(win,text="Change Password",command=Change_Password,fg="black",bg="white",font=("calibri",15,"bold"))
b4.place(x=20,y=300)
b5=Button(win,text="Feedback",command=Feedback,fg="black",bg="white",font=("calibri",15,"bold"))
b5.place(x=20,y=350)
b6=Button(win,text="Logout",command=Logout,fg="black",bg="white",font=("calibri",15,"bold"))
b6.place(x=20,y=400)
b7=Button(win,text="<==",command=Back,fg="black",bg="red",font=("calibri",15,"bold"))
b7.place(x=550,y=450)

win.mainloop()         
             
