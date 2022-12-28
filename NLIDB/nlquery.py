import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from Apps.entry import cur_db
import random
from ottp import smtObj
from tkinter import simpledialog
from nltk.tokenize import sent_tokenize, word_tokenize
from corpuss import store, tables, dept, values


root = Tk()
root.geometry("800x800")
root.title("Natural Language Interfaces to Database")


loginPage = LabelFrame(root, text="Login", bg="ivory", bd=10, font=("Arial", 20))
loginPage.pack(fill="both", expand="yes", padx=150, pady=250)

l1 = Label(loginPage, text="Username", font=("Arial, Bold", 15), bg="ivory")
l1.place(x=50, y=20)

username = StringVar()
e1 = Entry(loginPage, width=30, bd=5, textvariable=username)
e1.place(x=180, y=20)

l4 = Label(loginPage, text="Password", font=("Arial, Bold", 15), bg="ivory")
l4.place(x=50, y=80)

password = StringVar()
e4 = Entry(loginPage, width=30, bd=5, textvariable=password, show='*')
e4.place(x=180, y=80)


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
            cursor2 = cur_db.fetchall()
            for i in cursor2:
                tables_user_have_access_to.append(i[0])
            print(tables_user_have_access_to)
            loginPage.pack_forget()

            logicPage = LabelFrame(root, text="Home", bg="ivory", bd=10, font=("Arial", 20))
            logicPage.pack(fill="both", expand="yes", padx=10, pady=20)

            l2 = Label(logicPage, text="Type Your Query Here", font=("Arial, Bold", 20))
            l2.place(x=150, y=20, width=500)

            nl_query = StringVar()
            e2 = Entry(logicPage, width=100, textvariable=nl_query)
            e2.place(x=80, y=80)

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

                table_name = ''
                column_name = ''
                value = ''

                # Extract table names
                t1, t2, t3 = "health", "payment", "student"

                if t1 in nlq:
                    table_name = tables[t1]
                elif t2 in nlq:
                    table_name = tables[t2]
                else:
                    table_name = tables[t3]

                # Extract column names
                for word in nlq:
                    if word in dept.keys():
                        column_name = dept[word]

                # Extract the value
                for word in nlq:
                    if word in values.keys():
                        value = values[word]

                # sql1 = f'select * from {table} where {column_name} = {value}'
                trv = ttk.Treeview(logicPage, selectmode='browse')
                trv.place(x=80, y=250, width=800, height=600)
                trv["columns"] = ("1", "2", "3", "4", "5")
                trv['show'] = 'headings'

                trv.column("1", width=10, anchor='c')
                trv.column("2", width=80, anchor='c')
                trv.column("3", width=80, anchor='c')
                trv.column("4", width=80, anchor='c')
                trv.column("5", width=80, anchor='c')

                trv.heading("1", text="")
                trv.heading("2", text="")
                trv.heading("3", text="")
                trv.heading("4", text="")
                trv.heading("5", text="")

                sn = 1

                # Checks if User have access to table
                if table_name in tables_user_have_access_to:

                    # Checks for Table Score
                    sql2 = "SELECT tscore FROM score WHERE tname = " + "\"" + table_name + "\""
                    cur_db.execute(sql2)
                    cursor3 = cur_db.fetchall()
                    for i in cursor3:
                        table_Score = i[0]
                        if table_Score == 0:
                            if column_name != '':
                                if table_name == "students":
                                    sql5 = "select student_id, name, course, level  from " + table_name + " where " + column_name + " = " + value
                                elif table_name == "payments":
                                    sql5 = "SELECT name, course, amount_paid, purpose FROM " + table_name + " p, students s where p.student_id = s.student_id and s." + column_name + " = " + value
                                else:
                                    sql5 = "select name, course, level, health_status from " + table_name + " m, students s where m.student_id = s.student_id and s." + column_name + " = " + value
                            else:
                                if table_name == "students":
                                    sql5 = "select student_id, name, course, level from " + table_name
                                elif table_name == "payments":
                                    sql5 = "SELECT name, course, amount_paid, purpose FROM " + table_name + " p, students s where p.student_id = s.student_id"
                                else:
                                    sql5 = "select name, course, level, health_status from " + table_name + " m, students s where m.student_id = s.student_id"

                            cur_db.execute(sql5)
                            cursor6 = cur_db.fetchall()
                            for i in cursor6:
                                trv.insert("", 'end', iid=i[0], values=(sn, i[0], i[1], i[2], i[3]))
                                sn += 1
                            print(sql5)
                        else:
                            sql4 = "select question, answer from quest where username = " + "\"" + user_details + "\""
                            cur_db.execute(sql4)
                            cursor5 = cur_db.fetchall()
                            for i in cursor5:
                                user_q = i[0]
                                user_a = i[1]
                            user_question = user_q
                            user_answer = user_a

                            user_input1 = simpledialog.askstring("Input", f'{user_question}')
                            if user_input1 == user_answer:
                                if column_name != '':
                                    if table_name == "students":
                                        sql5 = "select student_id, name, course, level  from " + table_name + " where " + column_name + " = " + value
                                    elif table_name == "payments":
                                        sql5 = "SELECT name, course, amount_paid, purpose FROM " + table_name + " p, students s where p.student_id = s.student_id and s." + column_name + " = " + value
                                    else:
                                        sql5 = "select name, course, level, health_status from " + table_name + " m, students s where m.student_id = s.student_id and s." + column_name + " = " + value
                                else:
                                    if table_name == "students":
                                        sql5 = "select student_id, name, course, level from " + table_name
                                    elif table_name == "payments":
                                        sql5 = "SELECT name, course, amount_paid, purpose FROM " + table_name + " p, students s where p.student_id = s.student_id"
                                    else:
                                        sql5 = "select name, course, level, health_status from " + table_name + " m, students s where m.student_id = s.student_id"

                                cur_db.execute(sql5)
                                cursor6 = cur_db.fetchall()
                                for i in cursor6:
                                    trv.insert("", 'end', iid=i[0], values=(sn, i[0], i[1], i[2], i[3]))
                                    sn += 1
                                print(sql5)
                            else:
                                messagebox.showinfo("Error", "Wrong Answer, You have been logged out!!!")
                                # Go to Log in Page
                else:
                    messagebox.showinfo("Error", "You don't have to access to this information")
                    # Return to Logic Page

            b2 = Button(logicPage, text="Submit", font=("Arial", 15), command=process)
            b2.place(x=380, y=150)

        else:
            messagebox.showinfo("Error", "Wrong Code")
    else:
        messagebox.showinfo("Error", "Wrong Credentials")
    # con_db.close()


b1 = Button(loginPage, text="Login", font=("Arial", 15), command=verify)
b1.place(x=200, y=120)

root.mainloop()
