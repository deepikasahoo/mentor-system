from tkinter import*
from tkinter import messagebox as mb
from subprocess import call
import mysql.connector
win=Tk()
win.geometry("600x600")

def Logout():
    win.destroy()
    call(["pyw","facultylogin.py"])
def Back():
    win.destroy()
    call(["pyw","facultylogin.py"])
def View_Complain_Status():
    win.destroy()
    call(["pyw","view complain status(faculty).py"])  
def Self_update():
    win.destroy()
    call(["pyw","facultyupdateform.py"])
def Update_Complain_Status():
    win.destroy()
    call(["pyw","update complain status(faculty).py"])
def Change_Password():
    win.destroy()
    call(["pyw","faculty changepassword.py"])
def Close():
    win.destroy()
    call(["pyw","welcomepage.py"])

l1=Label(win,text="MENTOR SYSTEM",fg="black",bg="lightgreen",font=("calibri",25,"bold"))
l1.place(x=150,y=20)
l2=Label(win,text="GUIDANCE FOR STUDENTS",fg="black",bg="pink",font=("calibri",15,"bold"))
l2.place(x=160,y=70)
l3=Label(win,text="FACULTY OPERATION",fg="black",font=("calibri",15,"bold"))
l3.place(x=170,y=100)

b1=Button(win,text="View Complain Status",command=View_Complain_Status,fg="black",bg="light yellow",font=("calibri",15,"bold"))
b1.place(x=100,y=150)
b2=Button(win,text="Self Update",command=Self_update,fg="black",bg="light yellow",font=("calibri",15,"bold"))
b2.place(x=100,y=200)
b3=Button(win,text="Change Password",command=Change_Password,fg="black",bg="light yellow",font=("calibri",15,"bold"))
b3.place(x=100,y=250)
b4=Button(win,text="Update Complain Status",command=Update_Complain_Status,fg="black",bg="light yellow",font=("calibri",15,"bold"))
b4.place(x=100,y=300)
b5=Button(win,text="Logout",fg="black",command=Logout,bg="light yellow",font=("calibri",15,"bold"))
b5.place(x=100,y=350)
'''b6=Button(win,text="Logout",fg="black",bg="light yellow",font=("calibri",15,"bold"))
b6.place(x=100,y=400)'''
b6=Button(win,text="<==",fg="black",command=Back,bg="red",font=("calibri",15,"bold"))
b6.place(x=550,y=500)
b6=Button(win,text="X",fg="black",command=Close,bg="red",font=("calibri",15,"bold"))
b6.place(x=0,y=0)

win.mainloop()         
             
