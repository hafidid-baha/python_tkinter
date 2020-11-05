from tkinter import *
from PIL import Image, ImageTk
# create the root window
root = Tk()
root.title("learn python with tkinter")
# chosing app icon
root.iconbitmap('img/spider.ico')

frame = LabelFrame(root, text="this is my frame", padx=50, pady=50)
frame.pack(padx=10, pady=10)

# putting a button inside the frame
btn = Button(frame, text="normale button")
btn.pack()
# keep the programme running intel the user close the app
root.mainloop()
