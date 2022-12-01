from tkinter import *
from PIL import Image, ImageTk
import random

# Window
root = Tk()
root.geometry('400x400')
root.title('Roll the Dice')


Label(root, text="").pack()  # This is for skipping a line
Label(root, text="Dice Roll Game", fg="antiquewhite", bg="aquamarine4", font="Roboto 16 bold italic").pack()

# images
dice_roll = ['dice1.png', 'dice2.png', 'dice3.png', 'dice4.png', 'dice5.png', 'dice6.png']
dice_img = ImageTk.PhotoImage(Image.open(random.choice(dice_roll)))
imgLabel = Label(root, image=dice_img)
imgLabel.image = dice_img  # To store the image
imgLabel.pack(expand=True)


def rolling_dice():
    dice_img = ImageTk.PhotoImage(Image.open(random.choice(dice_roll)))
    imgLabel.configure(image=dice_img)   # update image
    imgLabel.image = dice_img


Button(root, text='Roll the Dice', fg='black', command=rolling_dice).pack(expand=True)
root.mainloop()
