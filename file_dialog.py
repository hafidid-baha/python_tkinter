from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
# create the root window
root = Tk()
root.title("learn python with tkinter")
# chosing app icon
root.iconbitmap('img/spider.ico')


def choseFile():
    global img  # using this to make the image reaable by the label
    # open the file dialog
    root.filename = filedialog.askopenfilename(
        initialdir="/Programming Projects/python/tinker/img", title="select a file", filetypes=(("png file", "*.png"), ("jpg files", "*.jpg")))
    Label(root, text=root.filename).pack()
    img = ImageTk.PhotoImage(Image.open(root.filename))
    Label(image=img).pack()


Button(root, text="chose a file", command=choseFile).pack()

# keep the programme running intel the user close the app
root.mainloop()
