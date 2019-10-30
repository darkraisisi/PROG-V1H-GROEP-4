from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()

w = '400'
h = '100'
root.geometry('{}x{}'.format(w, h))
root.configure(background='#FCC63F')

label = Label(root, text="Welkom bij NS", background='#FCC63F',
            foreground='#212B5C',
            font=('Helvetica', 16, 'bold italic'),
            width=14,
            height=3)

label.grid(column=0, row=0)
root.columnconfigure(0, weight=1)

img = ImageTk.PhotoImage(Image.open("../images/ns-logo.jpg"))
label2 = Label(root, image=img)
label2.grid(column=0, row=1)

button3 = Button(master=root, text='Toon reisinformatie', bg='#212B5C',font=('Helvetica', 23, 'bold'))
button3.grid(row=2, column=0, pady=32)

root.mainloop()

