from tkinter import *
from PIL import Image, ImageTk
# create the root window
root = Tk()
root.title("learn python with tkinter")
# chosing app icon
root.iconbitmap('img/spider.ico')

counter = 0

# get the image object
image1 = ImageTk.PhotoImage(Image.open("img/1.jpg"))
image2 = ImageTk.PhotoImage(Image.open("img/2.jpg"))
image3 = ImageTk.PhotoImage(Image.open("img/3.jpg"))
image4 = ImageTk.PhotoImage(Image.open("img/4.jpg"))

image_list = [image1, image2, image3, image4]
# show the image on the label
label = Label(image=image_list[0])
label.grid(row=0, column=0, columnspan=3)
status_label = Label(
    root, text=f"image {counter+1} / {len(image_list)}", bd=1, relief=SUNKEN, anchor=E)
status_label.grid(row=2, column=0, columnspan=3,
                  sticky=W+E)


def replace_image(index):
    global label
    label.grid_forget()
    label = Label(image=image_list[index])
    label.grid(row=0, column=0, columnspan=3)


def next():
    global counter
    global label
    if counter < len(image_list)-1:
        counter = counter + 1
    replace_image(counter)
    upadate_status()


def prev():
    global counter
    global label
    if counter > 0:
        counter = counter - 1
    replace_image(counter)
    upadate_status()


def upadate_status():
    global counter
    global status_label
    global image_list
    status_label.grid_forget()
    status_label = Label(
        root, text=f"image {counter+1} / {len(image_list)}", bd=1, relief=SUNKEN, anchor=E)
    status_label.grid(row=2, column=0, columnspan=3,
                      sticky=W+E)


back_btn = Button(root, text="<<", command=lambda: prev())
exit_btn = Button(root, text="Exit", command=root.quit)
next_btn = Button(root, text=">>", command=lambda: next())


back_btn.grid(row=1, column=0)
exit_btn.grid(row=1, column=1)
next_btn.grid(row=1, column=2)


# keep the programme running intel the user close the app
root.mainloop()
