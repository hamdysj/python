from tkinter import *

main_window = Tk()

# Labels
Label(main_window, text="A Simple Calculator").grid(row=0, columnspan=4)
# Text Input
entry = Entry(main_window, width=50, borderwidth=5)
entry.grid(row=1, columnspan=4, padx=0)

num = []


def number(val):
    # This hold the value temporary
    value = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(value) + str(val))


def clear_input():
    num.clear()
    entry.delete(0, END)


def list_of_input(val):
    num1 = entry.get()
    num.append(int(num1))
    entry.delete(0, END)

    sign = entry.get(val)
    return sign


def equals():
    num1 = entry.get()
    num.append(int(num1))
    entry.delete(0, END)

    sum_up = 0
    for i in num:
        sum_up += int(i)

    entry.insert(0, sum_up)


# Buttons

Button(main_window, text="1", padx=40, pady=20, command=lambda: number(1)).grid(row=2, column=0)
Button(main_window, text="2", padx=40, pady=20, command=lambda: number(2)).grid(row=2, column=1)
Button(main_window, text="3", padx=40, pady=20, command=lambda: number(3)).grid(row=2, column=2)
Button(main_window, text="+", padx=40, pady=20, command=lambda: list_of_input("+")).grid(row=2, column=3)

Button(main_window, text="4", padx=40, pady=20, command=lambda: number(4)).grid(row=3, column=0)
Button(main_window, text="5", padx=40, pady=20, command=lambda: number(5)).grid(row=3, column=1)
Button(main_window, text="6", padx=40, pady=20, command=lambda: number(6)).grid(row=3, column=2)
Button(main_window, text="-", padx=40, pady=20).grid(row=3, column=3)

Button(main_window, text="7", padx=40, pady=20, command=lambda: number(7)).grid(row=4, column=0)
Button(main_window, text="8", padx=40, pady=20, command=lambda: number(8)).grid(row=4, column=1)
Button(main_window, text="9", padx=40, pady=20, command=lambda: number(9)).grid(row=4, column=2)
Button(main_window, text="*", padx=40, pady=20).grid(row=4, column=3)

Button(main_window, text="0", padx=40, pady=20, command=lambda: number(0)).grid(row=5, column=0)
Button(main_window, text="=", padx=40, pady=20, command=equals).grid(row=5, column=1)
Button(main_window, text="CLEAR", padx=40, pady=20, command=clear_input).grid(row=5, column=2)
Button(main_window, text="/", padx=40, pady=20).grid(row=5, column=3)

main_window.mainloop()
