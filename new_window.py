from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
# create the root window
root = Tk()
root.title("learn python with tkinter")
# chosing app icon
root.iconbitmap('img/spider.ico')


def openWindow():
    # to create new window
    win = Toplevel()
    win.title("secound window")
    win.iconbitmap('img/spider.ico')
    Label(win, text="new window text").pack()


Button(root, text="open secound window",
       command=openWindow).pack(padx=20, pady=20)

# keep the programme running intel the user close the app
root.mainloop()
