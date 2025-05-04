# Changing Window Favicon

from tkinter import *
w = Tk()
w.geometry('500x500')
w.title('New window GUI')

icon_var = PhotoImage(file='valorant.png')
w.iconphoto(True,icon_var)

# icon_var to convert Png to PhotoImage, by mentioning the file name
# 2 parameters in iconphoto function, True and icon_var

w.mainloop()

# NOTE : tkinter doesn't support png