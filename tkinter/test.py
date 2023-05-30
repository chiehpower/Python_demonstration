"""
Source: https://shengyu7697.github.io/python-tkinter-tutorial/
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk

def button_event():
    mybutton['text'] = 'hello world'

root = tk.Tk()
root.geometry('300x300')
root.title('hello world')


mylabel = tk.Label(root, text='hello world', font=('Arial', 18))
# mylabel.grid(row=0, column=0)

# mylabel.pack()

mybutton = tk.Button(root, text='button', command=button_event)
# mybutton.grid(row=0, column=0)

# mybutton.pack()

mylabel = tk.Label(root, text='Name:')
mylabel.grid(row=0, column=0)
myentry = tk.Entry(root)
myentry.grid(row=0, column=1)

mylabel2 = tk.Label(root, text='Password:')
mylabel2.grid(row=1, column=0)
myentry2 = tk.Entry(root, show='*')
myentry2.grid(row=1, column=1)

mybutton = tk.Button(root, text='Login')
mybutton.grid(row=2, column=1)

root.mainloop()