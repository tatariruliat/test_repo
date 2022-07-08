import tkinter as tk

# Create instance
parent = tk.Tk()

lbl = tk.Label(parent, text="Привет")
lbl.grid(column=0, row=0)

# Add a title
parent.title("Сообщение для Пушинки")

# Start GUI
parent.mainloop()

# More about Tkinter
# https://pythonru.com/uroki/obuchenie-python-gui-uroki-po-tkinter


# Changes