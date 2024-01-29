from tkinter import*
from subprocess import call
import mysql.connector
from tkinter import messagebox as mb

win=Tk()
win.geometry("500x500")
def Submit():
    if len(t1.get())==0:
       mb.showinfo("warning","Complain status is blank please enter")
       t1.focus_set()
    elif len(t2.get())==0:
        mb.showinfo("warning","Update status is blank please enter")
        t1.focus_set()

    else:
        conn=mysql.connector.connect(host="localhost",username="root",password="deepika21",database="world")
        cur=conn.cursor()
        cur.execute("select * from complainregform where Complain_id=%s and Complain_Status=%s",(t1.get(),t2.get()))
        results=cur.fetchall()
        if len(results)!=0:
            Complain_id=t1.get();
            Update_status=t3.get();

            sql="Update complainregform set complain_Status=%s where Complain_id=%s";
            val=(Update_status,Complain_id)
            cur.execute(sql,val)

            conn.commit()
            mb.showinfo("","Updated successfully")
        else:
            mb.showerror("","Wrong Complain_id & Complain_Status")
            
    
def Clear():
    t1.delete(0,END)
    t2.delete(0,END)
    t3.delete(0,END)
    t1.focus_set()
def Close():
    win.destroy()
    call(["pyw","welcomepage.py"])
def Back():
    win.destroy()
    call(["pyw","faculty operation.py"])
    

l1=Label(win,text="MENTOR SYSTEM",fg="black",bg="light green",font=("calibri",20,"bold"))
l1.place(x=150,y=20)
l2=Label(win,text="GUIDANCE FOE STUDENTS",fg="black",bg="pink",font=("calibri",15,"bold"))
l2.place(x=140,y=60)
l3=Label(win,text="UPDATE COMPLAIN STATUS",fg="blue",bg="light yellow",font=("calibri",15,"bold"))
l3.place(x=130,y=95)

complain_id=Label(win,text="Complain id:",fg="black",font=("calibri",15,"bold"))
complain_id.place(x=50,y=150)
t1=Entry(win,fg="black",font=("calibri",15,"bold"))
t1.place(x=195,y=150)
complain_status=Label(win,text="Complain Status:",font=("calibri",15,"bold"))
complain_status.place(x=50,y=200)
t2=Entry(win,fg="black",font=("calibri",15,"bold"))
t2.place(x=195,y=200)
update_status=Label(win,text="Update Status:",font=("calibri",15,"bold"))
update_status.place(x=50,y=250)
t3=Entry(win,fg="black",font=("calibri",15,"bold"))
t3.place(x=195,y=250)

var=IntVar()
rb1=Radiobutton(win,text="Pending",value=1,variable=var)
rb1.place(x=150,y=300)
rb2=Radiobutton(win,text="Close",value=2,variable=var)
rb2.place(x=220,y=300)

submit_button=Button(win,text="SUBMIT",command=Submit,fg="black",bg="light blue",font=("calibri",15,"bold"))
submit_button.place(x=130,y=360)
cancel_button=Button(win,text="CLEAR",command=Clear,fg="black",bg="light blue",font=("calibri",15,"bold"))
cancel_button.place(x=250,y=360)
close_button=Button(win,command=Close,text="X",bg="red",font="bold")
close_button.place(x=0,y=0)

Back=Button(win,command=Back,text="<==",fg="black",bg="red",font="bold")
Back.place(x=390,y=450)
                                                                 






win.mainloop()
