from tkinter import *

# create the root window
root = Tk()
# create text input to catch data from users
e = Entry(root, width=20, bg="#eee", fg="black")
e.pack()
# put default text
e.insert(0, "enter your name")

# create event function


def btnEvent():
    status = Label(root, text="the ebtered name is "+e.get())
    status.pack()


# create a button inside root window
mbtn = Button(root, text="show name", padx=50, pady=10, command=btnEvent)

# add button to the screen
mbtn.pack()
# keep the programme running intel the user close the app
root.mainloop()
