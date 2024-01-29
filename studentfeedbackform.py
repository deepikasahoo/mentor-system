
from tkinter import *
from tkinter import ttk
from subprocess import call
from tkinter import messagebox
import mysql.connector

win=Tk()
win.geometry("600x600")

def Back():
    win.destroy()
    call(["pyw","Student operation.py"])
def Cancel():
    t1.delete(0,END)
    t2.delete(0,END)
    
def Submit():

    if len(t1.get())==0:
        messagebox.showinfo("warning","Studentid is blank please enter")
        t1.focus_set()

    elif len(t2.get())==0:
        messagebox.showinfo("warning","Password is blank please enter")
        t2.focus_set()
    
    elif feedback_list.get() == "select":
        messagebox.showinfo("","feedback not selected")

    else:
        conn = mysql.connector.connect(user='root', password='deepika21', host='localhost', database='world')
        cur=conn.cursor()

        Student_id=t1.get();
        Password=t2.get();
        Rate_Your_Feedback=feedback_list.get();
        sql="insert into feedbackform values(%s,%s,%s)";
        val=(Student_id,Password,Rate_Your_Feedback)
        cur.execute(sql,val)
        conn.commit()
        messagebox.showinfo("","Submit successfully")    
    


l1=Label(win,text="MENTOR SYSTEM",fg="black",bg="light green",font=("calibri",20,"bold"))
l1.place(x=150,y=20)
l2=Label(win,text="GUIDANCE FOR STUDENTS",fg="black",bg="pink",font=("calibri",15,"bold"))
l2.place(x=140,y=60)
l3=Label(win,text="STUDENT FEEDBACK FORM",fg="black",bg="yellow",font=("calibri",15,"bold"))
l3.place(x=130,y=95)

student_id=Label(win,text="Student id:",fg="black",font=("calibri",18,"bold"))
student_id.place(x=70,y=150)
t1=Entry(win,fg="black",bg="white",font=("calibri",18,"bold"))
t1.place(x=200,y=150)
password=Label(win,text="Password:",fg="black",font=("calibri",18,"bold"))
password.place(x=70,y=200)
t2=Entry(win,show="*",fg="black",bg="white",font=("calibri",18,"bold"))
t2.place(x=200,y=200)

feedback_list=Label(win,text="Rate Your Feedback",fg="black",font=("calibri",18,"bold"))
feedback_list.place(x=150,y=250)
feedback_list=ttk.Combobox(win,values=["EXCELLENT","GOOD","AVERAGE"])
feedback_list["state"]="readonly"
feedback_list.set("--select--")
feedback_list.place(x=170,y=290)

submit_button=Button(win,text="SUBMIT",command=Submit,fg="black",bg="light blue",font=("calibri",12,"bold"))
submit_button.place(x=170,y=350)
cancel_button=Button(win,text="CANCEL",command=Cancel,fg="black",bg="light blue",font=("calibri",12,"bold"))
cancel_button.place(x=260,y=350)
back_button=Button(win,command=Back,text="<==",fg="black",bg="red",font=("calibri",12,"bold"))
back_button.place(x=450,y=400)


win.mainloop()
