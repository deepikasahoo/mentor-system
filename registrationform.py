from tkinter import*
from tkinter import ttk
from subprocess import call
from tkinter import messagebox as mb

win=Tk()
win.geometry("600x700")
def Back():
    win.destroy()
    call(["pyw","welcomepage.py"])

l1=Label(win,text="MENTOR SYSTEM",fg="black",bg="lightgreen",font=("calibri",20,"bold"))
l1.place(x=150,y=20)

l2=Label(win,text="Guidance For Students",fg="black",bg="lightpink",font=("calibri",15,"bold"))
l2.place(x=150,y=70)


l3=Label(win,text="Admin Registration form",fg="black",font=("calibri",15,"bold"))
l3.place(x=140,y=100)

l4=Label(win,text="Employee id:",fg="black",font=("calibri",15,"bold"))
l4.place(x=50,y=150)

l5=Label(win,text="Full Name:",fg="black",font=("calibri",15,"bold"))
l5.place(x=50,y=180)
l6=Label(win,text="User id:",fg="black",font=("calibri",15,"bold"))
l6.place(x=50,y=210)
l7=Label(win,text="Password:",fg="black",font=("calibri",15,"bold"))
l7.place(x=50,y=240)
l7=Label(win,text="Mobile no.:",fg="black",font=("calibri",15,"bold"))
l7.place(x=50,y=270)
l8=Label(win,text="Email id:",fg="black",font=("calibri",15,"bold"))
l8.place(x=50,y=300)
l9=Label(win,text="Aadhaar no.:",fg="black",font=("calibri",15,"bold"))
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

var=IntVar()
gender_rb1=Radiobutton(win,text="Male",value=1,variable=var)
gender_rb1.place(x=170,y=365)
gender_rb2=Radiobutton(win,text="Female",value=2,variable=var)
gender_rb2.place(x=230,y=365)
gender_rb3=Radiobutton(win,text="Others",value=3,variable=var)
gender_rb3.place(x=300,y=365)

bloodgroup=Label(win,text="BloodGroup:",fg="black",font=("calibri",15,"bold"))
bloodgroup.place(x=50,y=390)
bloodgroup_list=ttk.Combobox(win,values=["O+","B-","AB+","B+","O-","AB+"])
bloodgroup_list["state"]="readonly"
bloodgroup_list.set("--Select--")
bloodgroup_list.place(x=170,y=395)


state=Label(win,text='State:',font=("calibri",15,"bold"))
state.place(x=50,y=420)
state_list=ttk.Combobox(win,values=["Odisha","Bihar","Assam","Bihar","Goa","Gujurat","Himachal Pradesh","Jharkhand","Karnatak","kerala","Punjab","Sikkim","West Bengal","Telengana"])
state_list["state"]="readonly"
state_list.set("--Select--")
state_list.place(x=170,y=425)

register_button=Button(win,text="Register",fg="black",bg="lightblue",font=("calibri",15,"bold"))
register_button.place(x=150,y=470)
clearall_button=Button(win,text="Cancel",fg="black",bg="lightblue",font=("calibri",15,"bold"))
clearall_button.place(x=250,y=470)
back_button=Button(win,text="<==",fg="black",command=Back,bg="red",font=("calibri",15,"bold"))
back_button.place(x=500,y=550)

win.mainloop()
