from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
# create the root window
root = Tk()
root.title("learn python with tkinter")
# chosing app icon
root.iconbitmap('img/spider.ico')
root.geometry("400x400")

checked = IntVar()


def show():
    Label(root, text=checked.get()).pack()


check = Checkbutton(root, text="please check me",
                    variable=checked, command=show)

# if you need to use string value
# check = Checkbutton(root, text="please check me",
#                     variable=checked,onvalue="on",offvalue="off", command=show)
# check.deselect()
check.pack()


# keep the programme running intel the user close the app
root.mainloop()
