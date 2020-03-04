from tkinter import *

root = Tk()

top_frame = Frame(root)
top_frame.pack()

bottom_frame = Frame(root)
bottom_frame.pack(side=BOTTOM)

button1 = Button(top_frame, text="Кнопка1", fg="red")
button2 = Button(top_frame, text="Кнопка2", fg="blue")
button3 = Button(top_frame, text="Кнопка3", fg="green")
button4 = Button(bottom_frame, text="Кнопка4", fg="gray")

button1.pack()
button2.pack()
button3.pack()
button4.pack()

root.mainloop()