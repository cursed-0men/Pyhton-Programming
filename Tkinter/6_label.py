# creating labels
# we use label function to create label with some parameters, like window name and text
# to display and position(center-top) label we use label_name.pack

from tkinter import *

w = Tk()
w.config(background='orange')
w.title("first label")
w.geometry('500x500')

label_var = Label(w,text="Hello World",
                  font=('JetBrains Mono',20,'bold'),
                  fg='blue',
                  bg="#5e9fff") # also mentioned font
# btw "fg" means foreground and it changes text color, also accepts hex-code
# "Bg" changes the background color of label
label_var.pack()

w.mainloop()