from tkinter import *

# create the root window
root = Tk()
root.title = "learn python with tkinter"
root.iconbitmap('E:/Programming Projects/python/tinker/img/spider.ico')

# create event function


def btnEvent():
    status = Label(root, text="the button is clicked")
    status.pack()


# create a button inside root window
mbtn = Button(root, text="click", padx=50, pady=10, command=btnEvent)

# add button to the screen
mbtn.pack()
# keep the programme running intel the user close the app
root.mainloop()
