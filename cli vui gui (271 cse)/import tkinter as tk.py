import tkinter as tk

def say_hello():
    label.config(text="Hello, Welcome to GUI!")

root = tk.Tk()
root.title("GUI Example")

button = tk.Button(root, text="Click Me", command=say_hello)
button.pack(pady=10)

label = tk.Label(root, text="")
label.pack(pady=10)

root.mainloop()
