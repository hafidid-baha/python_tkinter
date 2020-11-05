from tkinter import *

# create the root window
root = Tk()
root.title("learn python with tkinter")
root.iconbitmap('E:/Programming Projects/python/tinker/img/spider.ico')

# create a label insde root window
mLabel = Label(root, text="hello world")
# adding label to the screen
mLabel.pack()

# keep the programme running intel the user close the app
root.mainloop()
