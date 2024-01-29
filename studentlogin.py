from tkinter import*
from subprocess import call
from tkinter import messagebox as mb
import mysql.connector

win=Tk()
win.geometry("600x600")

def Login():
    if len(t1.get())==0:
        mb.showinfo("warning","Username is Blank Please Enter")
        t1.focus_set()
    elif len(t2.get())==0:
         mb.showinfo("warning","Password is Blank Please Enter")
         t2.focus_set()
    else:
        Userid=t1.get();
        Password=t2.get();


    conn=mysql.connector.connect(host="localhost",username="root",password="deepika21",database="world")
    cur=conn.cursor()
    sql="select * from stdregdform where Userid=%s and Password=%s"
    cur.execute(sql,[(Userid),(Password)])
    results=cur.fetchall()
    
    if results:
        '''mb.showinfo("","Login Successfully")'''
        win.destroy()
        call(["pyw","student operation.py"])
    else:
        mb.showinfo("","Login Failed")
            

def Back():
    win.destroy()
    call(["pyw","welcomepage.py"])
def registration():
    win.destroy()
    call(["pyw","student registrationform.py"])
def Cancel():
    t1.delete(0,END)
    t2.delete(0,END)
    t1.focus_set()
def Close(): 
    win.destroy()
    call(["pyw","welcomepage.py"])
    
    


l1=Label(win,text="MENTOR SYSTEM",fg="black",bg="lightgreen",font=("calibri",20,"bold"))
l1.place(x=150,y=20)

l2=Label(win,text="GUIDANCE FOR STUDETNS",fg="black",bg="pink",font=("calibri",15,"bold"))
l2.place(x=130,y=60)

l3=Label(win,text="STUDENT LOGIN",fg="black",bg="light yellow",font=("calibri",15,"bold"))
l3.place(x=170,y=95)

l4=Label(win,text="Username:",fg="black",font=("calibri",15,"bold"))
l4.place(x=50,y=150)

l5=Label(win,text="Password:",fg="black",font=("calibri",15,"bold"))
l5.place(x=50,y=200)

t1=Entry(win,fg="black",bg="white",font=("calibri",15,"bold"))
t1.place(x=150,y=150)
t2=Entry(win,show="*",fg="black",bg="white",font=("calibri",15,"bold"))
t2.place(x=150,y=200)


b1=Button(win,text="Login",command=Login,fg="black",bg="light yellow",font=("calibri",15,"bold"))
b1.place(x=160,y=250)
b2=Button(win,command=Cancel,text="Cancel",fg="black",bg="light yellow",font=("calibri",15,"bold"))
b2.place(x=250,y=250)
b3=Button(win,text="Registration",fg="black",command=registration,bg="light blue",font=("calibri",15,"bold"))
b3.place(x=160,y=350)


l5=Label(win,text="Are you a new user? if yes then click on Registration",fg="black",font=("calibri",12,"bold"))
l5.place(x=50,y=300)

b5=Button(win,text="<==",command=Back,fg="black",bg="Red",font=("calibri",15,"bold"))
b5.place(x=380,y=390)

b6=Button(win,text="X",command=Close,fg="black",bg="Red",font=("calibri",15,"bold"))
b6.place(x=0,y=0)

win.mainloop()         


             



