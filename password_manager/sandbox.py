from tkinter import *

window = Tk()

r_label = Label(bg="red", width=20, height=5)
r_label.grid(row=0, column=0)

g_label = Label(bg="green", width=20, height=5)
g_label.grid(row=1, column=1)

b_label = Label(bg="blue", width=40, height=5)
b_label.grid(row=2, column=0, columnspan=2)
window.mainloop()