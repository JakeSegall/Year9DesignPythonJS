from tkinter import *

root =Tk()

#w = tk.Label( text="Swimming Distance Calculator", fg="white")
top_label = Label( root,text="Swimming Distance Calculator", bg="white",fg=
"black",font=("Helvetica", 20))
top_label.place(x=60,y=20)
#top_label.pack()

"""text=Text( root, height=1, width=50)
text.insert(END,"convert now")
text.pack()"""
def perform_convert():

	print("good job")

convert_btn=Button(root,text="Convert Now!!", highlightbackground="#a9a9a9", command=perform_convert)
#convert_btn.pack()
convert_btn.place(x=100,y=70)



short_course_input=Entry(root)
short_course_input.delete(0, END)
short_course_input.insert(0, "Enter Time(SC)")
short_course_input.place(x=60,y=100)

long_course_input=Entry(root)
long_course_input.delete(0, END)
long_course_input.insert(0, "Enter Time(LC)")
long_course_input.place(x=60,y=150)

converted_time=Entry(root)
converted_time.delete(0, END)
converted_time.insert(0, "Converted Time")
converted_time.place(x=270,y=100)

converted_time1=Entry(root)
converted_time1.delete(0, END)
converted_time1.insert(0, "Converted Time")
converted_time1.place(x=270,y=150)

dist_type = IntVar()
Radiobutton(root, text="Meters",  bg=("#243c6c"), variable=dist_type, value="meters").place(x=60, y=210)
Radiobutton(root, text="Yards",  bg=("#243c6c"), variable=dist_type, value="yards").place(x=180, y=210)

High_contrast = IntVar()
Radiobutton(root, text="High Contrast", bg=("#243c6c"), variable=High_contrast, value="High Contrast").place(x=300, y=210)
 
def showImg(self):
	load = Image.open('UCC.png') 
	render = ImageTK.PhotoImage(load)

	img = Label(Self, image=render)
	img.imgage = render
	img.place(x=300,y=300)

root.title("Swimming time converter")
root.geometry("500x300")
root.configure(background='#243c6c')
root.mainloop()