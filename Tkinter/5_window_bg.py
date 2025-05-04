# changing background color

from tkinter import *
w = Tk()
w.geometry('500x500')
w.title('New bg color')

# changing icon
icon = PhotoImage(file='valorant.png')
w.iconphoto(True,icon)

# changing Bg color
w.config(background='orange') # we can mention color name or hex-code

w.mainloop()