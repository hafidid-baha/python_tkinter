from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
# create the root window
root = Tk()
root.title("learn python with tkinter")
# chosing app icon
root.iconbitmap('img/spider.ico')
root.geometry("400x400")

vertical = Scale(root, from_=0, to=100)
vertical.pack()


def slide(value):
    val_label = Label(root, text=value)
    val_label.pack()


horizontal = Scale(root, from_=0, to=100, orient=HORIZONTAL,
                   command=slide)
horizontal.pack()
# keep the programme running intel the user close the app
root.mainloop()
