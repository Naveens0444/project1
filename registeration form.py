from tkinter import *
from tkinter import ttk
window = Tk()
window.title("welcome to registeration form")
window.geometry("450x300")
window.configure(background = "red")
a = Label(window ,text = "First name").grid(row = 0, column = 0)
b = Label(window ,text = "Last name").grid(row = 1, column = 0)
c = Label(window ,text = "Email id").grid(row = 2, column = 0)
d = Label(window ,text = "Password").grid(row = 3 ,column = 0)
e = Label(window ,text = "contact no").grid(row = 4, column = 0)
a1 = Entry(window).grid(row = 0,column = 1)
b1 = Entry(window).grid(row = 1,column = 1)
c1 = Entry(window).grid(row = 2,column = 1)
d1 = Entry(window).grid(row = 3,column = 1)
e1 = Entry(window).grid(row = 4,column = 1)
def clicked():
    res ="welcome to" + txt.get()
    lbl.configure(text = res)
btn=ttk.Button(window,text="submit").grid(row = 5,column=  0)
window.mainloop()