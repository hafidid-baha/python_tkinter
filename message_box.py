from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
# create the root window
root = Tk()
root.title("learn python with tkinter")
# chosing app icon
root.iconbitmap('img/spider.ico')
# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno


def showInfo():
    messagebox.showinfo("this is my title", "hello world this is my info")


def showWarning():
    messagebox.showwarning("this is my title", "Warning message")


def showError():
    messagebox.showerror("this is my title", "error message")


def askQuestion():
    messagebox.askquestion("this is my title", "are you ready")


def askOkCancel():
    messagebox.askokcancel(
        "this is my title", "ar you sure you want to delete this item")


def askYesNo():
    # anser variable holds the returned result from the message box
    answer = messagebox.askyesno(
        "this is my title", "yes no question")


Button(root, text="show Info message",
       command=askYesNo).pack(padx=50, pady=20)

# keep the programme running intel the user close the app
root.mainloop()
