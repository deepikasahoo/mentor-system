import mysql.connector
from tkinter import *
from tkinter import messagebox
from subprocess import call

win=Tk()
win.geometry("450x400")
win.config(bg="pink")

def View():
    if len(t1.get())==0:
        messagebox.showinfo("warning","Complain_id is blank please enter")
        t1.focus_set()
    else:
        Complain_id=t1.get();
        conn=mysql.connector.connect(host="localhost",username="root",password="deepika21",database="world")
        cur=conn.cursor()
        sql="select * from complainregform where Complain_id=%s"
        cur.execute(sql,[(Complain_id)])
        results=cur.fetchall()
    if results:
        messagebox.showinfo("","View successfully")
        win.destroy()
        call(["pyw","view complain status(faculty).py"])

    else:
        messagebox.showinfo("","View failed")
    
       
def Back():
    win.destroy()
    call(["pyw","Student operation.py"])


l1=Label(win,text="MENTOR SYSTEM",fg="black",bg="lightgreen",font=("calibri",20,"bold"))
l1.place(x=130,y=30)
l2=Label(win,text="Guidance For Students",fg="black",bg='yellow',font=("calibri",18,"bold"))
l2.place(x=120,y=70)
l1=Label(win,text="VIEW COMPLAIN STATUS(STUDENT)",fg="blue",bg='pink',font=("calibri",15,"bold"))
l1.place(x=80,y=100)
l1=Label(win,text="Complain id:",fg="black",bg='pink',font=("calibri",17,"bold"))
l1.place(x=90,y=160)

t1=Entry(win,fg='black',bg='white',bd=5)
t1.place(x=230,y=165)

conn=mysql.connector.connect(host="localhost",username="root",password="deepika21",database="world")
cursor=conn.cursor()
cursor.execute("SELECT * from complainregform")
r=cursor.fetchall()

conn.close()

b1=Button(win,text="VIEW",bg='blue',fg='white',command=View,bd=3)
b1.place(x=150,y=280)
b1=Button(win,text="CANCEL",bg='blue',fg='white',bd=3)
b1.place(x=220,y=280)
b1=Button(win,text="<==",bg='red',fg='black',command=Back,bd=3)
b1.place(x=350,y=350)


win.mainloop()
