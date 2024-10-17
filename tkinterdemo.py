# intsall step in linux
# sudo apt install python3-tk

import tkinter

win=tkinter.Tk()
win.title("Sajan")
win.configure(bg="green")
win.minsize(400,400)
win.maxsize(600,600)

l1=tkinter.Label(win,text='Welcome',bg='blue',fg='white')
l1.pack() #to allign a text or a label to the center

'''l2=tkinter.Label(win,text='Welcome',bg='blue',fg='white')
l2.place(x=100,y=50) # too place a text or label with the help of x and y direction

l3=tkinter.Label(win,text='Welcome',bg='blue',fg='white')
l3.grid(row=2,column=2) # it can only be set by a grid one by one in an order we cannot place a text in between the grids'''

# form creation
def save():
    l3.config(text=e1.get())

l2=tkinter.Label(win,text='name')
l2.place(x=75,y=20)

e1=tkinter.Entry(win)
e1.place(x=150,y=20)

btn=tkinter.Button(win,text='submit',bg='blue',activebackground='lightblue',activeforeground='green',padx=2,pady=2,command=save)
btn.place(x=170,y=40)

l3=tkinter.Label(win)
l3.place(x=170,y=90)

win.mainloop()