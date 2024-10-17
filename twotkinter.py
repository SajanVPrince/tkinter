import tkinter

win=tkinter.Tk()
win.title("Sajan")
win.configure(bg="green")
win.minsize(400,400)
win.maxsize(600,600)

l1=tkinter.Label(win,text='Login',bg='blue',fg='white')
l1.pack() #to allign a text or a label to the center

# form creation
def save():
    win1=tkinter.Tk()
    win1.title("Sajan")
    win1.configure(bg="green")
    win1.minsize(400,400)
    win1.maxsize(600,600)
    l1=tkinter.Label(win1,text='Login',bg='blue',fg='white')
    l1.pack()
    l2=tkinter.Label(win1,text='Username')
    l2.place(x=75,y=20)

    l3=tkinter.Label(win1,text='Password')
    l3.place(x=75,y=40)

    e1=tkinter.Entry(win1)
    e1.place(x=150,y=20)

    e2=tkinter.Entry(win1)
    e2.place(x=150,y=40)    
    
    btn2=tkinter.Button(win1,text='submit')
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

btn=tkinter.Button(win,text='subit',bg='blue',activebackground='lightblue',activeforeground='green',padx=2,pady=2)

btn1=tkinter.Button(win,text='register',bg='blue',activebackground='lightblue',activeforeground='green',padx=2,pady=2,command=save)
btn.place(x=190,y=80)
btn1.place(x=200,y=120)

win.mainloop() 
