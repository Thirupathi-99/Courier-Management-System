from tkinter import *
import sqlite3
from tkinter import messagebox

top = Tk()
top.title("CMS-Home")
top.geometry("1350x650")

user = StringVar()
pasw = StringVar()
c=0

def login_info():
    user1 = user.get()
    passw = pasw.get()
    conn=sqlite3.connect("file.db")
    c=conn.cursor()
    c.execute("select username,password from student2")
    p=c.fetchall()
    for i in p:
        if ((user1==i[0]) and (passw==i[1])):
            print("succesfull login")
            book()
            c=1
    if(c==0):
        print("Invalid Login")

dest = StringVar()
type = StringVar()
weight = IntVar()

def book():

    count=0
    top.title("Book ")
    top.geometry("1350x650")
    label = Label(top, height=500, width=500)
    label.place(x=0, y=0)

    frame11 = Frame(top, relief='flat', bd=10)
    frame11.place(x=500, y=30)
    frame11.configure(background='lightgreen')
    l11 = Label(frame11, font=('', 30, 'bold', 'underline'), text="Booking Form ", bd=10)
    l11.pack()

    des = Label(top, text="Destination", font=('bold', 15, 'italic'), width=10)
    des.place(x=450, y=220)
    d = Entry(top, textvar=dest, bd=7)
    d.place(x=670, y=220)

    type = Label(top, text="Type ", font=('bold', 15, 'italic'), width=10)
    type.place(x=450, y=260)
    t = Entry(top, textvar=type, bd=7)
    t.place(x=670, y=260)

    wei = Label(top, text="Weight ", font=('bold', 15, 'italic'), width=10)
    wei.place(x=450, y=300)
    w = Entry(top, textvar=weight, bd=7)
    w.place(x=670, y=300)
    rf = top.register(correct)
    w.configure(validate="key", validatecommand=(rf, '%P'))

    book = Button(top, text="Confirm", width=10, font=('', 10, 'bold'), command=database1)
    book.place(x=670, y=350)

    lo = Button(top, text="Logout", width=10, font=('', 10, 'bold'), command=login)
    lo.place(x=890, y=350)
    
    lo = Button(top, text="Bill", width=10, font=('', 10, 'bold'), command=bill)
    lo.place(x=780, y=350)
    
    top.mainloop()

def correct(inp):
    if inp.isdigit():
        return True
    elif inp is "":
        return True
    else:
        return False
    
def bill():
    wei=weight.get()
    bill=20*wei;
    messagebox.showinfo("Bill","Amount Payable is %s\nPayment Mode : Offline\nPayable at our nearest store"%bill);

ph = IntVar()
no = IntVar()
#count=1362
from random import *
def msg_box():
    
    wei=weight.get()
    bill=20*wei;
    
    count1=randint(500,10000)
    messagebox.showinfo("Confirmation","Your courier has been successfully booked")
    messagebox.showinfo("Booked","Consignment No.is '%s'"%count1)
    messagebox.showinfo("Bill","Amount Payable is %s\nPayment Mode : Offline\nPayable at our nearest store"%bill);
d=0
def status():
   
    top.title("Status")
    top.geometry("1350x650")

    mob = ph.get()
    print(mob)
    con = no.get()
    conn=sqlite3.connect("file.db")
    c=conn.cursor()
    c.execute("select mobile,name from student2")
    m=c.fetchall()
    
    for k in m:
        if (mob==int(k[0])):
            messagebox.showinfo("Tracking Information","Mobile No : %s \nBooked on : 13 November\nStatus: Shipped at 11:00 am\nExcepted time of Arrival : 17 November"%k[0])
            d=1
    if(d==0):
        messagebox.showinfo("Tracking Information","Mobile Number does not exist");
        
    top.mainloop()

def track1():

    top.title("Track Consigment")
    top.geometry("1350x650")
    label = Label(top, height=500, width=500)
    label.place(x=0, y=0)

    frame1 = Frame(top, relief='flat', bd=10)
    frame1.place(x=450,y=30)
    frame1.configure(background='lightgreen')
    l1 = Label(frame1, font=('', 30, 'italic', 'underline'), text="Track Consignment", bd=10)
    l1.pack()

    mobile = Label(top, text="Mobile No ", font=('bold', 15,'italic'),width=10)
    mobile.place(x=420, y=180)
    mobil = Entry(top, textvar=ph,bd=7)
    mobil.place(x=660, y=180)

    m = top.register(correct)
    mobil.configure(validate="key", validatecommand=(m, '%P'))

    consig = Label(top, text="Consign No ", font=('bold', 15,'italic'),width=10)
    consig.place(x=420, y=230)
    consige = Entry(top, textvar=no,bd=7)
    consige.place(x=660, y=230)

    tr = Button(top, text='Track', width=10, font=('', 10, 'bold'), command=status)
    tr.place(x=660, y=270)

    lo = Button(top, text="Logout", width=10, font=('', 10, 'bold'), command=login)
    lo.place(x=830, y=270)
    
    top.mainloop()

Name = StringVar()
RegNo = IntVar()
var = IntVar()
Mobile = IntVar()
Email = StringVar()
Userr = StringVar()
Passwordr = StringVar()

def database():
    name1 = Name.get()
    nl=len(name1)
    email1 = Email.get()
    el=len(email1)
    gender = var.get()
    mobil = Mobile.get()
    regi = RegNo.get()
    usern=Userr.get()
    pswd=Passwordr.get()
    if(nl>0):
     if(regi>0):
      if(gender>0):
       if((mobil>5000000000) and (mobil<9999999999)):
        if(el>0):
           
            conn = sqlite3.connect("file.db")
            #with conn:
            cursor = conn.cursor()
            #cursor.execute('drop table student2');
            cursor.execute('CREATE TABLE  student2 (Name TEXT,RegNo TEXT,Gender TEXT,Mobile TEXT,Email TEXT,username TEXT,password TEXT)')
            cursor.execute('INSERT INTO student2 (Name,RegNo,Gender,Mobile,Email,username,password) VALUES (?,?,?,?,?,?,?)',
            (name1, regi, gender, mobil, email1, usern, pswd))
            #cursor.execute("select * from student2")
            #a=cursor.fetchall()
            #print(a)
            print(" Registration Successfull")
            conn.commit()
            login()
        
        else:
            print(" email id must be filled")
       else:
            print("mobile no must be 10 digits")
      else:
            print("kindly select your gender")
     else:
            print("Registration no must be filled")
    else:
            print("Name must be filled")


def database1():
    dest1 = dest.get()
    dl = len(dest1)
    type1 = type.get()
    t = len(type1)
    weight1 = weight.get()

    if (dl > 0):
            if (weight1 > 0):

                        conn = sqlite3.connect("book.db")
                        cursor = conn.cursor()
                        cursor.execute('drop table book')
                        cursor.execute('CREATE TABLE book (destination TEXT,type TEXT,weight TEXT)')
                        cursor.execute('INSERT INTO book (destination,type,weight) VALUES (?,?,?)',(dest1,type1,weight1))
                        print("Booking Successfull")
                        conn.commit()
                        msg_box()
                        track1()

            else:
                print("kindly enter the weight")
    else:
        print("Destination must be filled")


def register():

    top.title("Register ")
    top.geometry("1350x650")
    label = Label(top, height=500, width=500)
    label.place(x=0, y=0)

    frame11 = Frame(top, relief='flat', bd=10)
    frame11.place(x=450,y=30)
    frame11.configure(background='lightgreen')
    l11 = Label(frame11, font=('', 30, 'bold', 'underline'), text="Registration Form", bd=10)
    l11.pack()

    name = Label(top, text="Name", font=('bold', 15,'italic'),width=10)
    name.place(x=450, y=220)
    n = Entry(top, textvar=Name, bd=7)
    n.place(x=670, y=220)

    regno = Label(top, text="Reg.No ", font=('bold', 15,'italic'),width=10)
    regno.place(x=450, y=260)
    re = Entry(top, textvar=RegNo,bd=7)
    re.place(x=670, y=260)
    r = top.register(correct)
    re.configure(validate="key", validatecommand=(r, '%P'))

    gender = Label(top, text="Gender ", font=('bold', 15,'italic'), width=10)
    gender.place(x=450, y=300)
    m = Radiobutton(top, text="Male", variable=var, value=1)
    m.place(x=670, y=300)
    f = Radiobutton(top, text="Female", variable=var, value=2)
    f.place(x=720, y=300)

    mob = Label(top, text="Mobile No ", font=('bold', 15,'italic'),width=10)
    mob.place(x=450, y=340)
    mobe = Entry(top, textvar=Mobile,bd=7)
    mobe.place(x=670, y=340)
    regs = top.register(correct)
    mobe.configure(validate="key", validatecommand=(regs, '%P'))

    email = Label(top, text="Email Id ", font=('bold', 15,'italic'),width=10)
    email.place(x=450, y=380)
    e = Entry(top, textvar=Email,bd=7)
    e.place(x=670, y=380)

    un = Label(top, text="User-Name ", font=('bold', 15, 'italic'), width=10)
    un.place(x=450, y=420)
    u = Entry(top, textvar=Userr,bd=7)
    u.place(x=670, y=420)

    pas = Label(top, text="Password ",font=('bold', 15, 'italic'), width=10)
    pas.place(x=450, y=460)
    p = Entry(top, show="*", textvar=Passwordr,bd=7)
    p.place(x=670, y=460)

    sub = Button(top, text="Submit", width=10, font=('', 10, 'bold'), command=database)
    sub.place(x=670, y=500)
    top.mainloop()


def login():
    
    top.title("Login Page")
    top.geometry("1350x650")

    label = Label(top, height=1350, width=650)
    label.place(x=0, y=0)

    frame1 = Frame(top, relief='flat', bd=10)
    frame1.place(x=550,y=30)
    frame1.configure(background='lightgreen')
    l1 = Label(frame1, font=('', 30, 'italic', 'underline'), text="Login Page", bd=10)
    l1.pack()

    id1 = Label(top, text="User-Name", font=('', 15, 'italic'), width=10)
    id1.place(x=480, y=230)
    pas = Label(top, text="Password" , font=('', 15, 'italic'), width=10)
    pas.place(x=480, y=280)

    ide = Entry(top, textvar=user,bd=7)
    ide.place(x=720, y=230)
    pase = Entry(top, show="*", textvar=pasw,bd=7)
    pase.place(x=720, y=280)

    log = Button(top,text='Login',width=10,font=('',10,'bold'),command=login_info)
    log.place(x=550, y=350)

    r = Button(top, text="New User",width=10,font=('',10,'bold'), command=register)
    r.place(x=720, y=350)

    top.mainloop()


label = Label(top, height=1350, width=650)
label.place(x=0, y=0)

canvas=Canvas(width=300,height=300)
canvas.pack(expand=YES,fill=BOTH)
gif1=PhotoImage(file = 'Capture.png')
canvas.create_image(80,0,image=gif1,anchor=NW)

la1=Label(top,font=('',15,'italic','underline'),text="Register :- New User",width=20,height=4,bd=2,relief='solid')
la1.configure(background='lightblue')
la1.place(x=520,y=200)
b1=Button(top,text='Click here',width=10,font=('',10,'bold'),command=register)
b1.place(x=590,y=265)

la2=Label(top,font=('',15,'italic','underline'),text="Login :- Existing User",width=20,height=4,bd=2,relief='solid')
la2.configure(background='lightblue')
la2.place(x=520,y=350)
b2=Button(top,text='Click here',width=10,font=('',10,'bold'),command=login)
b2.place(x=590,y=415)

la3=Label(top,font=('',15,'italic','underline'),text="Track Consignment",width=20,height=4,bd=2,relief='solid')
la3.configure(background='lightblue')
la3.place(x=520,y=500)
b3=Button(top,text='Click here',width=10,font=('',10,'bold'),command=track1)
b3.place(x=590,y=565)

frame1=Frame(top,relief='flat',bd=10)
frame1.place(x=390,y=30)
frame1.configure(background='lightgreen')
l1=Label(frame1,font=('',30,'italic','underline'),text="Courier Management System",bd=10)
l1.pack()

top.mainloop()
