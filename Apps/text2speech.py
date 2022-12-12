from tkinter import *
from gtts import gTTS
from playsound import playsound

root = Tk()
root.geometry("350x300")
root.configure(bg='ghost white')
root.title("DataFlair - TEXT TO SPEECH")

Label(root, text="TEXT_TO_SPEECH", font="arial 20 bold", bg='white smoke').pack()

msg = StringVar()
Label(root, text="Enter Text", font='arial 15 bold', bg='white smoke').place(x=20, y=60)
Entry(root, textvariable=msg, width='50').place(x=20, y=100)


def Text_to_speech():
    message = msg.get()
    speech = gTTS(text=message)
    speech.save('message.mp3')
    playsound('message.mp3')


def Exit():
    root.destroy()


def Reset():
    msg.set("")


Button(root, text="PLAY", font='arial 15 bold', command=Text_to_speech, width='4').place(x=25, y=140)
Button(root, font='arial 15 bold', text='EXIT', width='4', command=Exit, bg='OrangeRed1').place(x=100, y=140)
Button(root, font='arial 15 bold', text='RESET', width='6', command=Reset).place(x=175, y=140)

root.mainloop()
