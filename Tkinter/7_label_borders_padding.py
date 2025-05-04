from tkinter import *

w = Tk()
w.title("Borders and padding")
w.geometry('500x500')

w.config(background="orange")

label = Label(w,
              text="Hello world",
              font=("JetBrains Mono",20,"bold"),
              fg = "Blue",
              bg = "#5e9fff",
              relief='solid', # border style
              bd = 2, # border width
              padx = 20, # x axis padding in label
              pady = 20 # y axis padding in label
              )

label.pack()

w.mainloop()

# start from 14.06