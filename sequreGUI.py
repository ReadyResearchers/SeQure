# a GUI for SeQure

from tkinter import Button
from tkinter import Canvas
import tkinter as tk
import os
import time
from tkinter.ttk import *
import subprocess

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

# defining open program
def run_program():
    path = 'terminalCode.py'
    #os.startfile('"%s"' % path)
    subprocess.run(["python", path])

def progress_bar():
    tasks = 10
    x = 0
    while(x<tasks):
        time.sleep(1)
        bar['value']+=10
        x+=1
        window.update_idletasks()

# creates a button
bar = Progressbar(window, length=300).pack(pady=10)
button = Button(window, text="Run checker.", command=run_program).pack(side='bottom')

title.pack()
canvas.pack()
window.mainloop()
