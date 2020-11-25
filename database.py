from tkinter import *
import sqlite3

# create the root window
root = Tk()
root.title("learn python with tkinter")
root.iconbitmap('E:/Programming Projects/python/tinker/img/spider.ico')
root.geometry("250x300")
connect = sqlite3.connect('address_book.db')


def submit():
    f_name.delete(0, END)
    l_name.delete(0, END)
    addr.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


# get the cursor
cursor = connect.cursor()
# create a table
# cursor.execute("""
#     CREATE TABLE addresss(
#         first_name text,
#         last_name text,
#         address text,
#         city text,
#         state text,
#         zipcode integer
#     )
# """)

# commit changes
connect.commit()

# close the connection
connect.close()

f_name = Entry(root, width=20)
f_name.grid(row=0, column=1)
Label(root, text="first name", width=10).grid(row=0, column=0)

l_name = Entry(root, width=20)
l_name.grid(row=1, column=1)
Label(root, text="first name", width=10).grid(row=1, column=0)

addr = Entry(root, width=20)
addr.grid(row=2, column=1)
Label(root, text="address", width=10).grid(row=2, column=0)

city = Entry(root, width=20)
city.grid(row=3, column=1)
Label(root, text="city", width=10).grid(row=3, column=0)

state = Entry(root, width=20)
state.grid(row=4, column=1)
Label(root, text="state", width=10).grid(row=4, column=0)

zipcode = Entry(root, width=20)
zipcode.grid(row=5, column=1)
Label(root, text="zip Code", width=10).grid(row=5, column=0)

Button(root, text="add number", command=submit).grid(row=6, column=0)

# keep the programme running intel the user close the app
root.mainloop()
