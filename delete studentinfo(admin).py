from tkinter import*
from tkinter import messagebox as mb
import mysql.connector
from subprocess import call


win=Tk()
win.geometry("600x600")
win.config(bg="black")
def Delete():
    if len(t1.get())==0:
        mb.showinfo("warning","studentid is blank please enter")
        t1.focus_set()
    else:
        studentid=t1.get();
        conn=mysql.connector.connect(host="localhost",username="root",password="deepika21",database="world")
        cur=conn.cursor()
        sql="select * from stdregdform where studentid=%s"
        cur.execute(sql,[(studentid)])
        results=cur.fetchall()
    if results:
        mb.showinfo("","studentid Deleted")
        win.destroy()
    else:
        mb.showinfo("","Incorrect student_id")
        conn.commit()

def Back():
    win.destroy()
    call(["pyw","admin operation.py"])
def Cancel():
    t1.delete(0,END)
    t1.focus_set()
    
    

l1=Label(win,text="MENTOR SYSTEM",fg="black",bg="lightgreen",font=("calibri",25,"bold"))
l1.place(x=150,y=20)
l2=Label(win,text="GUIDANCE FOR STUDENTS",fg="black",bg="pink",font=("calibri",15,"bold"))
l2.place(x=160,y=70)
l3=Label(win,text="DELETE STUDENT INFORMATION",fg="black",bg="#FFCF81",font=("calibri",15,"bold"))
l3.place(x=139,y=110)
l4=Label(win,text="studentid:",fg="black",font=("calibri",15,"bold"))
l4.place(x=80,y=180)
t1=Entry(win,fg="black",bg="white",font=("calibri",15,"bold"))
t1.place(x=200,y=180)
b1=Button(win,text="Delete",command=Delete,fg="black",bg="white",font=("calibri",15,"bold"))
b1.place(x=180,y=250)
b2=Button(win,text="Cancel",command=Cancel,fg="black",bg="white",font=("calibri",15,"bold"))
b2.place(x=280,y=250)



b3=Button(win,text="<==",command=Back,fg="black",bg="red",font=("calibri",15,"bold"))
b3.place(x=550,y=500)

win.mainloop()         
             
