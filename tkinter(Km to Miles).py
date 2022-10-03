from tkinter import *
import tkinter as tk

root = tk.Tk()
root.title("Mile To Km Converter")
root.minsize(width=400, height=200)
root.config(padx=80, pady=50)
 
label1 = tk.Label(text="Miles")
label1.grid(column=2, row=0)
 
label2 = tk.Label(text="is equal to")
label2.grid(column=0, row=1)
 
label3 = tk.Label(text="Km")
label3.grid(column=2, row=1)
 
label4 = tk.Label(text=0)
label4.grid(column=1, row=1)
 
 
def calc():
    miles = int(entry.get())
    km = round(miles * 1.609)
    label4.config(text=f"{km}")
 
 
button = tk.Button(text="Calculate", command=calc)
button.grid(column=1, row=2)
 
 
entry = tk.Entry()
entry.grid(column=1, row=0)
 
 
root.mainloop()
