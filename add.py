import  tkinter as tk
from tkinter import *
import screens as UI
import os
from PIL import ImageTk, Image

dirname = os.path.dirname(os.path.realpath(__file__))

# core

root = tk.Tk()
root.minsize(900, 450)
root.maxsize(900, 450)
root.title('Autentifikimi')

# icon 
root.iconbitmap(dirname + '/icon.ico')
canvas = tk.Canvas(root, width=800, height=500)
canvas.pack()
menu = UI.menu(root, canvas)

#image resize
image = Image.open(dirname + '/Sistemi.png')
new_image = image.resize((250, 250))
new_image.save(dirname + '/Sistemi4.png')

#image on the left
leftside = ImageTk.PhotoImage(Image.open('Sistemi4.png'))
Mylabel1 = Label(image=leftside).place(x=50,y=90)

UI.loginP(root, canvas, menu)
root.mainloop()
