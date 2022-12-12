from tkinter import *
from tkinter import messagebox
from entry import *

root = Tk()
root.title("Library")
root.minsize(width=400, height=400)
root.geometry("600x500")

same = True
n = 0.25
# Adding a background image
Canvas1 = Canvas(root)
# Canvas1.create_image(300, 340, image=img)
# Canvas1.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight)
Canvas1.pack(expand=True, fill=BOTH)

headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
headingLabel = Label(headingFrame1, text="Welcome to \n DataFlair Library", bg='black', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


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
    root.destroy()


def addBook():
    global book_info1, book_info2, book_info3, book_info4, bookTable, root


    root = Tk()
    root.title("Add Book")
    root.minsize(width=400, height=400)
    root.geometry("600x500")


    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.3, rely=0.05, relwidth=0.5, relheight=0.1)
    headingLabel = Label(headingFrame1, text="Add Books", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    bodyFrame = Frame(root, bg="black", bd=5)
    bodyFrame.place(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.37)

    book_info1 = StringVar()
    book_info2 = StringVar()
    book_info3 = StringVar()
    book_info4 = StringVar()

    Label(bodyFrame, text="Book ID:", fg='white', bg="black", font=('Courier', 8)).place(relx=0.02, rely=0.1,
                                                                                         relwidth=0.31,
                                                                                         relheight=0.1)
    Entry(bodyFrame, textvariable=book_info1, fg='black', bg='white', font=('Courier', 10)).place(relx=0.37, rely=0.1,
                                                                                                  relwidth=0.6,
                                                                                                  relheight=0.1)

    Label(bodyFrame, text="Title:", fg='white', bg="black", font=('Courier', 8)).place(relx=0.02, rely=0.25,
                                                                                       relwidth=0.31,
                                                                                       relheight=0.1)
    Entry(bodyFrame, textvariable=book_info2, fg='black', bg='white', font=('Courier', 10)).place(relx=0.37, rely=0.25,
                                                                                                  relwidth=0.6,
                                                                                                  relheight=0.1)

    Label(bodyFrame, text="Author:", fg='white', bg="black", font=('Courier', 8)).place(relx=0.02, rely=0.4,
                                                                                        relwidth=0.31,
                                                                                        relheight=0.1)
    Entry(bodyFrame, textvariable=book_info3, fg='black', bg='white', font=('Courier', 10)).place(relx=0.37, rely=0.4,
                                                                                                  relwidth=0.6,
                                                                                                  relheight=0.1)

    Label(bodyFrame, text="Status(Avail/Issued):", fg='white', bg="black", font=('Courier', 8)).place(relx=0.02,
                                                                                                      rely=0.55,
                                                                                                      relwidth=0.31,
                                                                                                      relheight=0.1)
    Entry(bodyFrame, textvariable=book_info4, fg='black', bg='white', font=('Courier', 10)).place(relx=0.37, rely=0.55,
                                                                                                  relwidth=0.6,
                                                                                                  relheight=0.1)

    Button(root, text="SUBMIT", font=('Courier', 15), command=bookRegister).place(relx=0.3, rely=0.75, relwidth=0.2,
                                                                                  relheight=0.1)
    Button(root, text="Quit", font=('Courier', 15), command=quit).place(relx=0.6, rely=0.75, relwidth=0.1,
                                                                        relheight=0.1)


def delete():
    pass


def view():
    pass


def issueBook():
    pass


def returnBook():
    pass


btn1 = Button(root, text="Add Book Details", bg='black', fg='white', command=addBook)
btn1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

btn2 = Button(root, text="Delete Book", bg='black', fg='white', command=delete)
btn2.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

btn3 = Button(root, text="View Book List", bg='black', fg='white', command=view)
btn3.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

btn4 = Button(root, text="Issue Book to Student", bg='black', fg='white', command=issueBook)
btn4.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)

btn5 = Button(root, text="Return Book", bg='black', fg='white', command=returnBook)
btn5.place(relx=0.28, rely=0.8, relwidth=0.45, relheight=0.1)

root.mainloop()

