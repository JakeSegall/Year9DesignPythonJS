import tkinter as tk

print("start program")
root = tk.Tk() #builds your own window. 

#widget/Element is an element in a GUI.
#button, textbox, input box, slider, drop down/
#Image,
btnl = tk.Button(root width = 100, height = 20)
#step-2: configure the widget 
btnl.config(text = "I am a button")
#step-3: place a wodget. 
btnl.pack()

output = tk.Text(root width = 100, height = 20)
output.config()
output.pack(fill = tk.BOTH)

root.mainloop()

print("END PROGRAM")