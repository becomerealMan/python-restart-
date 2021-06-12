#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import tkinter as tk
calc=tk.Tk()
calc.geometry("300x300")
calc.title("계산기")

display=tk.Entry(calc, width=20)

def func(event):
    result=eval(tk.Entry.get(display))
    print(result)
    display.delete(0,tk.END)
    display.insert(0,result)
    
display = tk.Entry(calc, width=20)
display.pack()

calc.bind('<Return>', func)
calc.mainloop()








 