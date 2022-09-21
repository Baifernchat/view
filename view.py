import tkinter as tk





app = tk.Tk()
app.title('Find')
app.geometry('400x400')

bs1 = tk.Label(master = app, text=" ")
bs1.pack()
title_1 = tk.Label(master = app, text="Enter point")
title_1.pack()

b1 = tk.Button(master = app, text="Enter point")
b1.pack()
app.mainloop()
