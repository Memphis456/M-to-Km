from tkinter import *

root = Tk()

def kg_converter():
    gram = float(number_input.get())*1000
    pound = float(number_input.get())*2.20462
    ounce = float(number_input.get())*35.274
    text1.delete("1.0", END)
    text1.insert(END, gram)
    text2.delete("1.0", END)
    text2.insert(END, pound)
    text3.delete("1.0", END)
    text3.insert(END, ounce)
    
number_input = StringVar()

label_1 = Label(root, text="Input the weight in KG")
label_1.grid(row = 0, column = 0)

label_2 = Entry(root, textvariable = number_input)
label_2.grid(row = 0, column = 1)

label_3 = Label(root, text="Gram")
label_3.grid(row = 1, column = 0)

label_4 = Label(root, text="Pound")
label_4.grid(row = 1, column = 1)

label_5 = Label(root, text="Ounce")
label_5.grid(row = 1, column = 2)

text1 = Text(root, height = 5, width = 30)
text1.grid(row = 2, column = 0)

text2 = Text(root, height = 5, width = 30)
text2.grid(row = 2, column = 1)

text3 = Text(root, height = 5, width = 30)
text3.grid(row = 2, column = 2)

button1 = Button(root, text = "Convert", command = kg_converter)
button1.grid(row = 0, column = 2)

root.mainloop()
