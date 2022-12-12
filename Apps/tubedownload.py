from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry("500x300")
root.resizable(0, 0)
root.title("Youtube Downloader ~ DataFlair")

Label(root, text="").pack
Label(root, text="Youtube Downloader", bg="blanchedalmond", fg="blue2", font="Enrequeta 15 bold").pack()

Label(root, text="Paste URL here", fg="blue").place(x=60, y=60)
url = StringVar()
Entry(root, textvariable=url, font="Enrequeta 15 bold", bg="beige").place(x=32, y=90)


def Downloader():
    link = YouTube(str(url.get()))
    video = link.streams.first()
    video.download()

    Label(root, text='Download Successfully', font='Enrequeta 15').place(x=180 , y=210)


Button(root,text='DOWNLOAD', font='arial 15 bold' , fg="blue", padx = 2, command=Downloader).place(x=180 ,y = 150)


root.mainloop()
