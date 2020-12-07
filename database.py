from tkinter import *
import sqlite3

# create the root window
root = Tk()
root.title("learn python with tkinter")
root.iconbitmap('E:/Programming Projects/python/tinker/img/spider.ico')
root.geometry("250x600")


def submit():
    connect = sqlite3.connect('address_book.db')
    # get the cursor
    cursor = connect.cursor()

    # create a query to insert new record to database
    cursor.execute("INSERT INTO addresss VALUES(:fname,:lname,:address,:city,:state,:zipcode)", {
        "fname": f_name.get(),
        "lname": l_name.get(),
        "address": addr.get(),
        "city": city.get(),
        "state": state.get(),
        "zipcode": zipcode.get(),
    })
    # commit changes
    connect.commit()
    # close the connection
    connect.close()

    f_name.delete(0, END)
    l_name.delete(0, END)
    addr.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


def query():
    connect = sqlite3.connect('address_book.db')
    # get the cursor
    cursor = connect.cursor()
    # select all the records
    cursor.execute("SELECT *,oid FROM addresss")
    addresses = cursor.fetchall()
    records = ""
    for address in addresses:
        records += str(address[0]+" "+address[1])+"\t"+str(address[6])+"\n"

    Label(root, text=records).grid(row=10, column=0, columnspan=2)
    # commit changes
    connect.commit()
    # close the connection
    connect.close()


def delete():
    connect = sqlite3.connect('address_book.db')
    # get the cursor
    cursor = connect.cursor()
    # select all the records
    # TODO: update for sql injection
    cursor.execute("DELETE FROM addresss WHERE oid="+delete_id.get())
    # commit changes
    connect.commit()
    # close the connection
    connect.close()

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


f_name = Entry(root, width=20)
f_name.grid(row=0, column=1)
Label(root, text="first name", width=10).grid(row=0, column=0)

l_name = Entry(root, width=20)
l_name.grid(row=1, column=1)
Label(root, text="last name", width=10).grid(row=1, column=0)

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


Button(root, text="Add New Record", command=submit).grid(
    row=6, column=0, columnspan=2, padx=10, pady=10, sticky=N+S+E+W)

Button(root, text="Show Record", command=query).grid(
    row=7, column=0, columnspan=2, padx=10, pady=10, sticky=N+S+E+W)

delete_id = Entry(root, width=20)
delete_id.grid(row=8, column=1)
Label(root, text="Record Id", width=10).grid(row=8, column=0)

Button(root, text="Delete Record", command=delete).grid(
    row=9, column=0, columnspan=2, padx=10, pady=10, sticky=N+S+E+W)


# keep the programme running intel the user close the app
root.mainloop()
