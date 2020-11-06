from tkinter import *
from PIL import Image, ImageTk
# create the root window
root = Tk()
root.title("learn python with tkinter")
# chosing app icon
root.iconbitmap('img/spider.ico')


def change_gender(gender):
    global gender_label
    gender_label.pack_forget()  # to remove old label
    gender_label = Label(root, text=gender)
    gender_label.pack()


gender = StringVar()
gender.set('male')

Radiobutton(root, text="male", value="male", variable=gender,
            command=lambda: change_gender(gender.get())).pack()
Radiobutton(root, text="female", value="female", variable=gender,
            command=lambda: change_gender(gender.get())).pack()

# create a label to show the selected gender
gender_label = Label(root, text=gender.get())
gender_label.pack()


# keep the programme running intel the user close the app
root.mainloop()
