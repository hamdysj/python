from tkinter import *


root = Tk()
root.geometry("400x350")
root.resizable(0, 0)
root.config(bg="#8E8E38")
root.title("Layouts")

Label(root, text="Box1", bg="#872657").place(x=20, y=20, relwidth=.3)
Label(root, text="Box2", bg="plum1").place(x=160, y=20, relwidth=.5)

Label(root, text="Box1", bg="#308014").place(x=50, y=110, relwidth=.3)
Label(root, text="Box2", bg="#5E2612").place(x=250, y=110, relwidth=.3)
Label(root, text="Box3", bg="#27408B").place(x=200, y=175, relwidth=.3, anchor='center')
Label(root, text="Box4", bg="#FF0000").place(x=50, y=220, relwidth=.3)
Label(root, text="Box5", bg="#551A8B").place(x=250, y=220, relwidth=.3)


root.mainloop()