from tkinter import*
from tkinter import messagebox as mb
from subprocess import call
import mysql.connector

win=Tk()
win.geometry("600x600")
win.config(bg="#B2A59B")
def Cancel():
    t1.delete(0,END)
    t2.delete(0,END)
    t3.delete(0,END)
    t4.delete(0,END)
    t1.focus_set()
    
    # TEST GIT
def Close():
    win.destroy()
    call(["pyw","welcomepage.py"])
def Back():
    win.destroy()
    call(["pyw","admin operation.py"])
def Changepassword():
    
    if len(t1.get())==0:
       mb.showinfo("warning","Password is blank please enter")
       t1.focus_set()
    elif len(t2.get())==0:
        mb.showinfo("warning","New_Password is blank please enter")
        t1.focus_set()
    elif len(t3.get())==0:
         mb.showinfo("warning","Confirm_Password is blank please enter")
    elif t3.get()!=t4.get():
        mb.showerror("warning","Password mismatch")
        
    else:
        conn=mysql.connector.connect(host="localhost",username="root",password="deepika21",database="world")
        cur=conn.cursor()
        cur.execute("select * from regform where Userid=%s and Password=%s",(t1.get(),t2.get()))
        results=cur.fetchall()
        if len(results)!=0:
            Userid=t1.get();
            New_Password=t3.get();

            sql="Update adminregform set Password=%s where Userid=%s";
            val=(New_Password,Userid)
            cur.execute(sql,val)

            conn.commit()
            mb.showinfo("","Password changed successfully")
        else:
            mb.showerror("","Wrong Userid& Password")
           
           
l1=Label(win,text="MENTOR SYSTEM",fg="black",bg="light green",font=("calibri",25,"bold"))
l1.place(x=150,y=50)
l2=Label(win,text="GUIDANCE FOR STUDENTS",fg="black",bg="light yellow",font=("calibri",20,"bold"))
l2.place(x=120,y=100)
l3=Label(win,text="CHANGE PASSWORD(ADMIN)",fg="black",bg="#B2A59B",font=("calibri",18,"bold"))
l3.place(x=105,y=140)

l4=Label(win,text="Userid",fg="black",bg="#B2A59B",font=("calibri",20,"bold"))
l4.place(x=60,y=200)
t1=Entry(win,fg="black",bg="white",font=("calibri",15,"bold"))
t1.place(x=280,y=205)
l5=Label(win,text="Password",fg="black",bg="#B2A59B",font=("calibri",20,"bold"))
l5.place(x=60,y=250)
t2=Entry(win,show="*",fg="black",bg="white",font=("calibri",15,"bold"))
t2.place(x=280,y=255)

l6=Label(win,text="New Password",fg="black",bg="#B2A59B",font=("calibri",20,"bold"))
l6.place(x=60,y=300)
t3=Entry(win,show="*",fg="black",bg="white",font=("calibri",15,"bold"))
t3.place(x=280,y=305)

l6=Label(win,text="Confirm Password",fg="black",bg="#B2A59B",font=("calibri",20,"bold"))
l6.place(x=60,y=350)
t4=Entry(win,show="*",fg="black",bg="white",font=("calibri",15,"bold"))
t4.place(x=280,y=355)

b1=Button(win,text="SAVE",fg="black",bg="light blue",command=Changepassword,font=("calibri",15,"bold"))
b1.place(x=200,y=410)
b2=Button(win,command=Cancel,text="CANCEL",fg="black",bg="light blue",font=("calibri",15,"bold"))
b2.place(x=280,y=410)
b3=Button(win,command=Back,text="<==",fg="black",bg="red",font=("calibri",15,"bold"))
b3.place(x=470,y=480)

b4=Button(win,text="X",command=Close,fg="black",bg="red",font=("calibri",15,"bold"))
b4.place(x=0,y=0)

win.mainloop()         
