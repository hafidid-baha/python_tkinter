from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
# create the root window
root = Tk()
root.title("learn python with tkinter")
# chosing app icon
root.iconbitmap('img/spider.ico')
root.geometry("400x400")

selected = StringVar()
# set the default value
selected.set('name')


def show():
    Label(root, text=selected.get()).pack()


menu = OptionMenu(root, selected, "name", "email",
                  "address", "telephon")
menu.pack()
# keep the programme running intel the user close the app
root.mainloop()
