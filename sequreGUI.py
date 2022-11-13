# for testVersions.py

from tkinter import Button
from tkinter import Canvas
import tkinter as tk

# creates window
window = tk.Tk()
window.geometry("500x250")

# widgets
title = tk.Label(text="SeQure")

# creates a canvas object
canvas = Canvas(window, width=450, height=200)
# add a text in canvas
canvas.create_text(225, 50, text="Welcome to SeQure!", fill="black")
canvas.create_text(225, 75, text="This is a plugin vulnerability checker!", fill="black")

# creates a button
button = Button(window, text="Run checker.", bd='5', command=window.destroy)

title.pack()
canvas.pack()
button.pack(side='bottom')
window.mainloop()
