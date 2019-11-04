import tkinter as tk

print("Hello")
root = tk.Tk()

btnl = tk.Button(root width = 100, height = 20)

btnl.config(text = "I am a button")

btnl.pack()

output = tk.Text(root width = 100, height = 20)
output.config()
output.pack(fill = tk.BOTH)

root.mainloop()

print("End")