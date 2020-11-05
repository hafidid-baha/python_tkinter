from tkinter import *
from PIL import Image, ImageTk
# create the root window
root = Tk()
root.title("learn python with tkinter")
# chosing app icon
root.iconbitmap('img/spider.ico')

# get the image object
image = ImageTk.PhotoImage(Image.open("img/y.png"))
# show the image on the label
label = Label(image=image)
label.pack()

# keep the programme running intel the user close the app
root.mainloop()
