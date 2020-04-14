from tkinter import *
from Var_and_Field import Var_Generator_GUI

root = Tk()
root.title("Генератор переменных")

entry1 = Entry(root, width=10, font=15)
entry2 = Entry(root, width=10, font=15)
entry3 = Entry(root, width=10, font=15)
entry4 = Entry(root, width=10, font=15)

button1 = Button(root, text="Генерировать")
label1 = Label(root, width=20, font=15)

entry1.grid(row=0, column=0)
entry2.grid(row=0, column=1)
entry3.grid(row=0, column=2)
entry4.grid(row=0, column=3)

button1.grid(row=0, column=4)
label1.grid(row=0, column=5)


def output():
    p1 = entry1.get()
    p2 = entry2.get()
    p3 = entry3.get()
    p4 = entry4.get()
    label1["text"] = Var_Generator_GUI.Rx_Cx(p1, p2, p3, p4)



button1.bind("<Button-1>", output)

root.mainloop()
