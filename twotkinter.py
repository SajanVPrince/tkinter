import tkinter
import sqlite3
# con=sqlite3.connect("tkinter/tkinter_data.db")
# try:
#     con.execute('create table sample(uname text,password text)')
# except:
#     pass

win=tkinter.Tk()
win.title("Sajan")
win.configure(bg="green")
win.minsize(400,400)
win.maxsize(600,600)

l1=tkinter.Label(win,text='Login',bg='blue',fg='white')
l1.pack() #to allign a text or a label to the center

# form creation
def home():
    win2=tkinter.Tk()
    l1=tkinter.Label(win,text='home page',bg='blue',fg='white')
    l1.pack() 
    btn1=tkinter.Button(win2,text='logout',command=win2.quit)
    btn1.place(x=40,y=20)


def login():
    con=sqlite3.connect("tkinter/tkinter_data.db")
    data=con.execute("select * from sample")
    f=0
    for i in data:
        if i[0]==e1.get() and i[1]==e2.get():
            f=1
            home()
    if f==0:
        l4.config(text="invalid")


def reg():
    win1=tkinter.Tk()
    win1.title("Sajan")
    win1.configure(bg="green")
    win1.minsize(400,400)
    win1.maxsize(600,600)

    def regi():
        con=sqlite3.connect("tkinter/tkinter_data.db")
        con.execute("insert into sample(uname,password)values(?,?)",(e1.get(),e2.get()))
        con.commit()
        win1.destroy()



    l1=tkinter.Label(win1,text='Register',bg='blue',fg='white')
    l1.pack()
    l2=tkinter.Label(win1,text='Username')
    l2.place(x=75,y=20)

    l3=tkinter.Label(win1,text='Password')
    l3.place(x=75,y=40)

    e1=tkinter.Entry(win1)
    e1.place(x=150,y=20)

    e2=tkinter.Entry(win1)
    e2.place(x=150,y=40)    
    
    btn2=tkinter.Button(win1,text='submit',command=regi)
    btn2.place(x=170,y=60)
    win1.mainloop()
 
l2=tkinter.Label(win,text='Username')
l2.place(x=75,y=20)

l3=tkinter.Label(win,text='Password')
l3.place(x=75,y=40)

e1=tkinter.Entry(win)
e1.place(x=150,y=20)

e2=tkinter.Entry(win)
e2.place(x=150,y=40)

btn=tkinter.Button(win,text='submit',bg='blue',activebackground='lightblue',activeforeground='green',padx=2,pady=2,command=login)

btn1=tkinter.Button(win,text='register',bg='blue',activebackground='lightblue',activeforeground='green',padx=2,pady=2,command=reg)
btn.place(x=190,y=80)
btn1.place(x=200,y=120)

l4=tkinter.Label(win)
l4.place(x=150,y=100)

win.mainloop() 
