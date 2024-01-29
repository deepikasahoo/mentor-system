from tkinter import*
from tkinter import ttk
from subprocess import call
import mysql.connector
from tkinter import messagebox as mb

win=Tk()
win.geometry("600x700")
'''def Admin():
    win.destroy()
    call(["python","adminlogin.py"])'''
def select():
    x=var.get()
    global genderselected;
    if x==1:
        genderselected="male"
    elif x ==2:
        genderselected="female"
    elif x==3:
        genderselected="others"    
    else:
        genderselected="error" 
def Back():
    win.destroy()
    call(["pyw","adminlogin.py"])
    
var=IntVar()
gender_rb1=Radiobutton(win,text="Male",value=1,command=select,variable=var)
gender_rb1.place(x=170,y=365)
gender_rb2=Radiobutton(win,text="Female",value=2,command=select,variable=var)
gender_rb2.place(x=230,y=365)
gender_rb3=Radiobutton(win,text="Others",value=3,command=select,variable=var)
gender_rb3.place(x=300,y=365)    
def update():

    if len(t1.get())==0:
        messagebox.showinfo("warning","Empid is blank please enter")
        t1.focus_set()

    elif len(t2.get())==0:
        messagebox.showinfo("warning","FullName is blank please enter")
        t2.focus_set()

    elif len(t3.get())==0:
        messagebox.showinfo("warning","Userid is blank please enter")
        t3.focus_set()

    elif len(t4.get())==0:
        messagebox.showinfo("warning","Password is blank please enter")
        t4.focus_set()

    elif len(t5.get())==0:
        messagebox.showinfo("warning","MobileNo is blank please enter")
        t5.focus_set()

    elif len(t6.get())==0:
        messagebox.showinfo("warning","Emailid is blank please enter")
        t6.focus_set()

    elif var.get() not in [1,2]:
        messagebox.showinfo("","Gender not selected")

    elif state_list.get() == "select":
        messagebox.showinfo("","State not selected")
        
    elif bloodgroup_list.get() == "select":
        messagebox.showinfo("","BloodGroup not selected")


    else:
        conn = mysql.connector.connect(user="root", password="deepika21", host="localhost", database="world")
        cur=conn.cursor()

    
        Empid=int(t1.get());
        FullName=t2.get();
        Userid=t3.get();
        Password=t4.get();
        MobileNo=t5.get();
        Emailid=t6.get();
        AadharNo=t7.get()
        genderselected;
        BloodGroup=bloodgroup_list.get();
        State=state_list.get();

        sql="insert into stdregform values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)";
        val=(Empid,FullName,Userid,Password,MobileNo,Emailid,AadharNo,genderselected,BloodGroup,State)

        cur.execute(sql,val)
        conn.commit()
        mb.showinfo("","update successfull")



l1=Label(win,text="MENTOR SYSTEM",fg="black",bg="lightgreen",font=("calibri",20,"bold"))
l1.place(x=160,y=20)

l2=Label(win,text="GUIDANCE FOR STUDENTS",fg="black",bg="lightpink",font=("calibri",15,"bold"))
l2.place(x=150,y=70)


l3=Label(win,text="SELF UPDATE FORM(STUDENT)",fg="black",font=("calibri",15,"bold"))
l3.place(x=135,y=100)




l4=Label(win,text="Studentidid:",fg="black",font=("calibri",15,"bold"))
l4.place(x=50,y=150)

l5=Label(win,text="Full Name:",fg="black",font=("calibri",15,"bold"))
l5.place(x=50,y=180)
l6=Label(win,text="Userid:",fg="black",font=("calibri",15,"bold"))
l6.place(x=50,y=210)
l6=Label(win,text="Password:",fg="black",font=("calibri",15,"bold"))
l6.place(x=50,y=240)
l7=Label(win,text="MobileNo.:",fg="black",font=("calibri",15,"bold"))
l7.place(x=50,y=270)
l8=Label(win,text="Emailid:",fg="black",font=("calibri",15,"bold"))
l8.place(x=50,y=300)
l9=Label(win,text="AadhaarNo.:",fg="black",font=("calibri",15,"bold"))
l9.place(x=50,y=330)

l10=Label(win,text="Gender:",fg="black",font=("calibri",15,"bold"))
l10.place(x=50,y=360)


t1=Entry(win,fg="black",bg="white",font=("calibri",15,"bold"))
t1.place(x=170,y=150)

t2=Entry(win,fg="black",bg="white",font=("calibri",15,"bold"))
t2.place(x=170,y=180)
t3=Entry(win,fg="black",bg="white",font=("calibri",15,"bold"))
t3.place(x=170,y=210)
t4=Entry(win,show='*',fg="black",bg="white",font=("calibri",15,"bold"))
t4.place(x=170,y=240)
t5=Entry(win,fg="black",bg="white",font=("calibri",15,"bold"))
t5.place(x=170,y=270)
t6=Entry(win,fg="black",bg="white",font=("calibri",15,"bold"))
t6.place(x=170,y=300)
t7=Entry(win,fg="black",bg="white",font=("calibri",15,"bold"))
t7.place(x=170,y=330)



bloodgroup=Label(win,text="BloodGroup:",fg="black",font=("calibri",15,"bold"))
bloodgroup.place(x=50,y=390)
bloodgroup_list=ttk.Combobox(win,values=["O+","B-","AB+","B+","O-","AB+"])
bloodgroup_list["state"]="readonly"
bloodgroup_list.set("--Select--")
bloodgroup_list.place(x=170,y=395)


state=Label(win,text='State:',font=("calibri",15,"bold"))
state.place(x=50,y=420)
state_list=ttk.Combobox(win,values=["Odisha","Bihar","Assam","Goa","Gujurat","Himachal Pradesh","Jharkhand","Karnatak","kerala","Punjab","Sikkim","West Bengal","Telengana"])
state_list["state"]="readonly"
state_list.set("--Select--")
state_list.place(x=170,y=425)

update_button=Button(win,text="Update",command=update,fg="black",bg="lightblue",font=("calibri",15,"bold"))
update_button.place(x=150,y=470)
clearall_button=Button(win,text="Cancel",fg="black",bg="lightblue",font=("calibri",15,"bold"))
clearall_button.place(x=250,y=470)
back_button=Button(win,text="<==",fg="black",command=Back,bg="red",font=("calibri",15,"bold"))
back_button.place(x=500,y=550)

win.mainloop()
