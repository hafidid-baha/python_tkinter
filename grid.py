from tkinter import *

# create the root window
root = Tk()
root.title("learn python with tkinter")
root.iconbitmap('E:/Programming Projects/python/tinker/img/spider.ico')

# create a label insde root window
username = Label(root, text="hafid id-baha")
userrole = Label(root, text="admin user")
# using grid instead of pack
username.grid(row=0, column=1)
userrole.grid(row=1, column=0)

# keep the programme running intel the user close the app
root.mainloop()
