from tkinter import *

root = Tk()
root.title = "learn python with tkinter"
root.iconbitmap('E:/Programming Projects/python/tinker/img/spider.ico')

e = Entry(root, borderwidth=5, width=35)
e.grid(row=0, column=0, columnspan=3)

button1 = Button(root, text=1, width=10, height=4,
                 command=lambda: button_click(1))
button2 = Button(root, text=2, width=10, height=4,
                 command=lambda: button_click(2))
button3 = Button(root, text=3, width=10, height=4,
                 command=lambda: button_click(3))

button4 = Button(root, text=4, width=10, height=4,
                 command=lambda: button_click(4))
button5 = Button(root, text=5, width=10, height=4,
                 command=lambda: button_click(5))
button6 = Button(root, text=6, width=10, height=4,
                 command=lambda: button_click(6))

button7 = Button(root, text=7, width=10, height=4,
                 command=lambda: button_click(7))
button8 = Button(root, text=8, width=10, height=4,
                 command=lambda: button_click(8))
button9 = Button(root, text=9, width=10, height=4,
                 command=lambda: button_click(9))
button0 = Button(root, text=0, width=10, height=4,
                 command=lambda: button_click(0))

buttonclear = Button(root, text="Clear", width=20,
                     height=4, command=lambda: clear())

buttonadd = Button(root, text="+", width=10, height=4,
                   command=lambda: button_add())
buttoneq = Button(root, text="=", width=20, height=4, command=lambda: equals())

button_subtruct = Button(root, text="-", width=10,
                         height=4, command=lambda: button_subtruct())
button_devide = Button(root, text="/", width=10,
                       height=4, command=lambda: button_dev())
button_multiply = Button(root, text="*", width=10,
                         height=4, command=lambda: button_multi())

button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)

button_devide.grid(row=5, column=0)
button_multiply.grid(row=5, column=1)
button_subtruct.grid(row=5, column=2)

button0.grid(row=4, column=0)
buttonclear.grid(row=4, column=1, columnspan=2)

buttonadd.grid(row=6, column=0)
buttoneq.grid(row=6, column=1, columnspan=2)


def button_add():
    global fnamber
    global operator
    operator = "add"
    fnamber = int(e.get())
    e.delete(0, END)


def button_multi():
    button_add()
    global operator
    operator = "multiply"


def button_subt():
    button_add()
    global operator
    operator = "subtruct"


def button_dev():
    button_add()
    global operator
    operator = "devistion"


def equals():
    # if(fnamber is None):
    #     fnamber = 0

    secound_number = int(e.get())
    e.delete(0, END)
    if operator == "add":
        e.insert(0, (fnamber+secound_number))
    elif operator == "multiply":
        e.insert(0, (fnamber*secound_number))
    elif operator == "subtruct":
        e.insert(0, (fnamber*secound_number))
    elif operator == "devistion":
        e.insert(0, (fnamber/secound_number))


def button_click(number):
    # e.delete(0, END)
    e.insert(len(e.get()), number)


def clear():
    e.delete(0, END)


root.mainloop()
