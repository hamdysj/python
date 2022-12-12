from tkinter import *
from tkinter import messagebox
from entry import *

root = Tk()
root.title("Add Book")
root.minsize(width=400, height=400)
root.geometry("600x500")

headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
headingFrame1.place(relx=0.3, rely=0.05, relwidth=0.5, relheight=0.1)
headingLabel = Label(headingFrame1, text="Add Books", bg='black', fg='white', font=('Courier', 15))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)


def bookRegister():
    bid = book_info1.get()
    title = book_info2.get()
    author = book_info3.get()
    status = book_info4.get()
    status = status.lower()

    bookTable = "books"

    insertBooks = "insert into " + bookTable + " values ('" + bid + "','" + title + "','" + author + "','" + status + "')"
    try:
        cur.execute(insertBooks)
        con.commit()
        messagebox.showinfo('Success', "Book added successfully")
    except:
        messagebox.showinfo("Error", "Can't add data into Database")

    print(bid)
    print(title)
    print(author)
    print(status)

    # root.destroy()


bodyFrame = Frame(root, bg="black", bd=5)
bodyFrame.place(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.37)

book_info1 = StringVar()
book_info2 = StringVar()
book_info3 = StringVar()
book_info4 = StringVar()

Label(bodyFrame, text="Book ID:", fg='white', bg="black", font=('Courier', 8)).place(relx=0.02, rely=0.1, relwidth=0.31,
                                                                                      relheight=0.1)
Entry(bodyFrame, textvariable=book_info1, fg='black', bg='white', font=('Courier', 10)).place(relx=0.37, rely=0.1,
                                                                                              relwidth=0.6,
                                                                                              relheight=0.1)

Label(bodyFrame, text="Title:", fg='white', bg="black", font=('Courier', 8)).place(relx=0.02, rely=0.25, relwidth=0.31,
                                                                                      relheight=0.1)
Entry(bodyFrame, textvariable=book_info2, fg='black', bg='white', font=('Courier', 10)).place(relx=0.37, rely=0.25,
                                                                                              relwidth=0.6,
                                                                                              relheight=0.1)

Label(bodyFrame, text="Author:", fg='white', bg="black", font=('Courier', 8)).place(relx=0.02, rely=0.4, relwidth=0.31,
                                                                                      relheight=0.1)
Entry(bodyFrame, textvariable=book_info3, fg='black', bg='white', font=('Courier', 10)).place(relx=0.37, rely=0.4,
                                                                                              relwidth=0.6,
                                                                                              relheight=0.1)

Label(bodyFrame, text="Status(Avail/Issued):", fg='white', bg="black", font=('Courier', 8)).place(relx=0.02, rely=0.55, relwidth=0.31,
                                                                                      relheight=0.1)
Entry(bodyFrame, textvariable=book_info4, fg='black', bg='white', font=('Courier', 10)).place(relx=0.37, rely=0.55,
                                                                                              relwidth=0.6,
                                                                                              relheight=0.1)

Button(root, text="SUBMIT", font=('Courier', 15), command=bookRegister).place(relx=0.3, rely=0.75, relwidth=0.2, relheight=0.1)
Button(root, text="Quit", font=('Courier', 15), command=quit).place(relx=0.6, rely=0.75, relwidth=0.1, relheight=0.1)


root.mainloop()