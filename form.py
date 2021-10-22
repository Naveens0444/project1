from tkinter import *
from tkinter import ttk
Window = Tk()
Window.title("Welcome to our page")
Window.geometry('500x400')
Window.configure(background = "black")
ttk.Button(Window, text = "hai, naveen").grid()
Window.mainloop()