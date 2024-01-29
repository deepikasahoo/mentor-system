from tkinter import*
from tkinter import messagebox as mb
from subprocess import call

win=Tk()
win.geometry("600x600")
def Logout():
    win.destroy()
    call(["pyw","adminlogin.py"])
def Back():
    win.destroy()
    call(["pyw","adminlogin.py"])
def View_Students_Information():
    win.destroy()
    call(["pyw","view student info.py"])  
def Self_update():
    win.destroy()
    call(["pyw","self update(admin).py"])
def Update_Student_Information():
    win.destroy()
    call(["pyw","studentupdateform.py"])  

def Delete_Student_Information():
    win.destroy()
    call(["pyw","delete Studentinfo(admin).py"])      
def Change_Password():
    win.destroy()
    call(["pyw","admin changepassword.py"])      
                
    

l1=Label(win,text="MENTOR SYSTEM",fg="black",bg="lightgreen",font=("calibri",25,"bold"))
l1.place(x=150,y=20)
l2=Label(win,text="Guidance For Students",fg="black",bg="pink",font=("calibri",15,"bold"))
l2.place(x=170,y=70)
l3=Label(win,text="Admin Operation",fg="black",font=("calibri",15,"bold"))
l3.place(x=190,y=100)

b1=Button(win,text="View Students Information",command=View_Students_Information,fg="black",bg="light yellow",font=("calibri",15,"bold"))
b1.place(x=100,y=150)
b2=Button(win,text="Update Student Information",command=Update_Student_Information,fg="black",bg="light yellow",font=("calibri",15,"bold"))
b2.place(x=100,y=200)
b3=Button(win,text="Delete Student Information",command=Delete_Student_Information,fg="black",bg="light yellow",font=("calibri",15,"bold"))
b3.place(x=100,y=250)
b4=Button(win,text="Change Password",command=Change_Password,fg="black",bg="light yellow",font=("calibri",15,"bold"))
b4.place(x=100,y=300)
b5=Button(win,text="Self Update",command=Self_update,fg="black",bg="light yellow",font=("calibri",15,"bold"))
b5.place(x=100,y=350)
b6=Button(win,text="Logout",command=Logout,fg="black",bg="light yellow",font=("calibri",15,"bold"))
b6.place(x=100,y=400)
b6=Button(win,text="<==",command=Back,fg="black",bg="red",font=("calibri",15,"bold"))
b6.place(x=550,y=500)

win.mainloop()         
             
