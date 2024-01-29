import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
from subprocess import call

win=Tk()
win.geometry("500x500")
win.config(bg="pink")

def registration():

    if len(t1.get())==0:
        messagebox.showinfo("warning","Student id is blank please enter")
        t1.focus_set()

    elif len(t2.get())==0:
        messagebox.showinfo("warning","Full name is blank please enter")
        t2.focus_set()
    elif len(t3.get())==0:
        messagebox.showinfo("warning","Roll no is blank please enter")
        t3.focus_set()

    elif len(t4.get())==0:
        messagebox.showinfo("warning","Complain id is blank please enter")
        t4.focus_set()

    elif len(t5.get())==0:
        messagebox.showinfo("warning","Complain details is blank please enter")
        t5.focus_set()
    elif len(t6.get())==0:
        messagebox.showinfo("warning","Complain Status is blank please enter")
        t5.focus_set()
    
    else:
        conn = mysql.connector.connect(user='root', password='deepika21', host='localhost', database='world')
        cur=conn.cursor()

        Student_id=t1.get();
        Full_name=t2.get();
        Roll_no=t3.get();
        Complain_id=t4.get();
        Complain_Details=t5.get();
        Complain_Status=t6.get();
        Complain_type=complain_list.get();
        sql="insert into complainregform values(%s,%s,%s,%s,%s,%s,%s)";
        val=(Student_id,Full_name,Roll_no,Complain_id,Complain_type,Complain_Details,Complain_Status)

        cur.execute(sql,val)
        conn.commit()
        messagebox.showinfo("","Registration successfully")



def Back():
    win.destroy()
    call(["pyw","student operation.py"])


l1=Label(win,text="MENTOR SYSTEM",fg="black",bg="lightgreen",font=("calibri",20,"bold"))
l1.place(x=130,y=30)
l2=Label(win,text="Guidance For Students",fg="black",bg='yellow',font=("calibri",18,"bold"))
l2.place(x=120,y=70)
l1=Label(win,text="COMPLAIN REGISTRATION FORM",fg="blue",bg='pink',font=("calibri",16,"bold"))
l1.place(x=87,y=110)
l1=Label(win,text="Student id:",fg="black",bg='pink',font=("calibri",17,"bold"))
l1.place(x=65,y=155)
l1=Label(win,text="Full Name",fg="black",bg='pink',font=("calibri",17,"bold"))
l1.place(x=65,y=190)
l1=Label(win,text="Roll no:",fg="black",bg='pink',font=("calibri",17,"bold"))
l1.place(x=65,y=227)
l1=Label(win,text="Complain id:",fg="black",bg='pink',font=("calibri",17,"bold"))
l1.place(x=65,y=260)
l1=Label(win,text="Complain type:",fg="black",bg='pink',font=("calibri",17,"bold"))
l1.place(x=65,y=293)
l1=Label(win,text="Complain Details:",fg="black",bg='pink',font=("calibri",17,"bold"))
l1.place(x=65,y=325)
l1=Label(win,text="Complain Status",fg="black",bg='pink',font=("calibri",17,"bold"))
l1.place(x=65,y=360)

t1=Entry(win,fg='black',bg='white',bd=5)
t1.place(x=260,y=160)
t2=Entry(win,fg='black',bg='white',bd=5)
t2.place(x=260,y=195)
t3=Entry(win,fg='black',bg='white',bd=5)
t3.place(x=260,y=228)
t4=Entry(win,fg='black',bg='white',bd=5)
t4.place(x=260,y=263)
t5=Entry(win,fg='black',bg='white',bd=5)
t5.place(x=260,y=327)
t6=Entry(win,fg='black',bg='white',bd=5)
t6.place(x=260,y=360)

complain_list=ttk.Combobox(win,values=['Books','Uniform','Academic','Library','Teacher','Education','Hostel'])
complain_list["state"]="readonly"
complain_list.set("--select--")
complain_list.place(x=260,y=298)

b1=Button(win,text="SUBMIT",bg='blue',fg='white',command=registration,bd=4)
b1.place(x=150,y=410)
b1=Button(win,text="CANCEL",bg='blue',fg='white',bd=4)
b1.place(x=220,y=410)
b1=Button(win,text="<==",command=Back,bg='red',fg='black',bd=4)
b1.place(x=380,y=450)



win.mainloop()
