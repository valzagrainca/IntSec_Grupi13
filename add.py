
import tkinter as tk
import os
import screens as UI

dirname = os.path.dirname(os.path.realpath(__file__))

# core

root = tk.Tk()
root.minsize(800, 500)
root.maxsize(800, 500)
root.title('Simple Authentication')
root.iconbitmap(dirname + '/icon.ico')
canvas = tk.Canvas(root, width=800, height=500)
canvas.pack()
menu = UI.create_menu(root, canvas)
UI.login_screen(root, canvas, menu)
root.mainloop()
