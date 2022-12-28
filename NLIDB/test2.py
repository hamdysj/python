import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Apps.entry import cur_db
import random
from ottp import smtObj
from tkinter import simpledialog
from nltk.tokenize import sent_tokenize, word_tokenize
from corpuss import store, tables, dept, values



class LoginPage(tk.Frame):
    def __init__(self, parent):
        # tk.Frame.__init__(self, parent)
        pass

    def login(self, parent, controller):
        tk.Frame.__init__(self, parent)
        border = tk.LabelFrame(self, text="Login", bg="ivory", bd=10, font=("Arial", 20))
        border.pack(fill="both", expand="yes", padx=150, pady=250)

        l1 = tk.Label(border, text="Username", font=("Arial, Bold", 15), bg="ivory")
        l1.place(x=50, y=20)

        username = tk.StringVar()
        e1 = tk.Entry(border, width=30, bd=5, textvariable=username)
        e1.place(x=180, y=20)

        l1 = tk.Label(border, text="Password", font=("Arial, Bold", 15), bg="ivory")
        l1.place(x=50, y=80)

        password = tk.StringVar()
        e1 = tk.Entry(border, width=30, bd=5, textvariable=password, show='*')
        e1.place(x=180, y=80)

        def verify():
            u = username.get()
            p = password.get()

            # sql1 = "SELECT username, pass FROM login WHERE username = \"hamdy\" and pass = \"123\""

            sql1 = "SELECT email, name, username FROM login WHERE username = " + "\"" + username.get() + "\"" + " and pass = \"" + password.get() + "\""
            cur_db.execute(sql1)
            cursor1 = cur_db.fetchall()
            if cursor1 != 0:
                for i in cursor1:
                    sendTo = i[0]
                    name = i[1]
                    user_name = i[2]
                    user_details = user_name

                sender = 'hamdysj@gmail.com'
                receiver = sendTo
                message = random.randint(000000, 999999)
                subject = 'OTP Verification.'
                msg = f'Subject: {subject}\n\n{message}'
                smtObj.sendmail(sender, receiver, msg)
                smtObj.quit()

                user_input = simpledialog.askinteger("Input", "Enter Your Verification Code")
                if user_input == message:

                    # Populates table names user have access to
                    tables_user_have_access_to = []
                    sql = "SELECT have_access FROM have_accessto WHERE username = " + "\"" + username.get() + "\""
                    cur_db.execute(sql)
                    cursor = cur_db.fetchall()
                    for i in cursor:
                        tables_user_have_access_to.append(i[0])

                    controller.show_frame(logic())
                else:
                    messagebox.showinfo("Error", "Wrong Code")
            else:
                messagebox.showinfo("Error", "Wrong Credentials")
            # con_db.close()

        b1 = tk.Button(border, text="Login", font=("Arial", 15), command=verify)
        b1.place(x=200, y=120)


class LogicPage(tk.Frame):
    def __init__(self, parent):
        # tk.Frame.__init__(self, parent)
        pass

    def logic(self, parent, controller):
        tk.Frame.__init__(self, parent)
        lp = LoginPage()

        l1 = tk.Label(self, text="Type Your Query Here", font=("Arial, Bold", 15))
        l1.place(x=150, y=20, width=500)

        nl_query = tk.StringVar()
        e1 = tk.Entry(self, width=100, textvariable=nl_query)
        e1.place(x=80, y=80)

        def process():
            # text = "Show all students in Computer Science"
            text = nl_query.get()
            text_token = word_tokenize(text)

            # Map word to corresponding word
            nlq = []
            for word in text_token:
                text_lower = word.lower()
                if text_lower in store.keys():
                    nlq.append(store[text_lower])
                else:
                    nlq.append('')

            tabless = ''
            column_name = ''
            value = ''

            # Extract table names
            t1, t2, t3 = "health", "paid", "student"

            if t1 in nlq:
                tabless = tables[t1]
            elif t2 in nlq:
                tabless = tables[t2]
            else:
                tabless = tables[t3]

            # Extract column names
            for word in nlq:
                if word in dept.keys():
                    column_name = dept[word]

            # Extract the value
            for word in nlq:
                if word in values.keys():
                    value = values[word]

            # sql1 = f'select * from {table} where {column_name} = {value}'
            trv = ttk.Treeview(self, selectmode='browse')
            trv.place(x=80, y=250, width=640)
            trv["columns"] = ("1", "2", "3", "4")
            trv['show'] = 'headings'

            trv.column("1", width=30, anchor='c')
            trv.column("2", width=150, anchor='c')
            trv.column("3", width=300, anchor='c')
            trv.column("4", width=80, anchor='c')

            trv.heading("1", text="S/No.")
            trv.heading("2", text="Matric Number")
            trv.heading("3", text="Name(s)")
            trv.heading("4", text="Level")
            sn = 1

            # Checks if User have access to table
            if tabless in self.access_t:

                # Checks for Table Score
                sql2 = "SELECT tscore FROM score WHERE tname = " + "\"" + tabless + "\""
                cur_db.execute(sql2)
                cursor2 = cur_db.fetchall()
                for i in cursor2:
                    table_Score = i[0]
                    if table_Score == 0:
                        if column_name != '':
                            sql1 = "select * from " + tabless + " where " + column_name + " = " + value
                        else:
                            sql1 = "select * from " + tabless
                        cur_db.execute(sql1)
                        cursor = cur_db.fetchall()
                        for i in cursor:
                            trv.insert("", 'end', iid=i[0], values=(sn, i[0], i[1], i[2]))
                    else:
                        sql3 = "select question, answer from quest where username " + "\"" + self.details + "\""
                        cur_db.execute(sql3)
                        cursor3 = cur_db.fetchall()
                        for i in cursor3:
                            user_q = i[0]
                            user_a = i[1]
                        user_question = user_q
                        user_answer = user_a

                        user_input1 = simpledialog.askinteger("Input", f'{user_question}')
                        if user_input1 == user_answer:
                            if column_name != '':
                                sql1 = "select * from " + tabless + " where " + column_name + " = " + value
                            else:
                                sql1 = "select * from " + tabless
                            cur_db.execute(sql1)
                            cursor = cur_db.fetchall()
                            for i in cursor:
                                trv.insert("", 'end', iid=i[0], values=(sn, i[0], i[1], i[2]))
                        else:
                            messagebox.showinfo("Error", "Wrong Answer, You have been logged out!!!")
                            controller.show_frame(LoginPage)
            else:
                messagebox.showinfo("Error", "You don't have to access to this information")
                controller.show_frame(LogicPage)

        b1 = tk.Button(self, text="Submit", font=("Arial", 15), command=process)
        b1.place(x=380, y=150)


class App(tk.Tk):
    def __init__(self, *args):
        tk.Tk.__init__(self, *args)

        # Create a Window for all
        window = tk.Frame(self)
        window.pack()

        window.grid_rowconfigure(0, minsize=800)
        window.grid_columnconfigure(0, minsize=800)

        self.frames = {}
        for f in (LoginPage, LogicPage()):
            frame = f(window, self)
            self.frames[f] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LoginPage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()


app = App()
app.mainloop()
