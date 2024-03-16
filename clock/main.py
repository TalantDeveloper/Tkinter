from tkinter import *
from time import *


def update():

    time_string = strftime('%I:%M:%S %p')
    time_label.config(text=time_string)

    day_string = strftime('%A')
    day_label.config(text=day_string)

    date_string = strftime('%B %d, %Y')
    date_label.config(text=date_string)

    time_label.after(1000, update)


window = Tk()
window.title('Clock')
window.geometry("480x320")
window.iconbitmap('clock.ico')

space_label = Label(window, text="")
space_label.pack()

space1_label = Label(window, text="")
space1_label.pack()

time_label = Label(window, font=('Helvetica', 50), fg='#00FF00', bg='black')
time_label.pack()

day_label = Label(window, font=('Times New Roman', 25))
day_label.pack()

date_label = Label(window, font=('Times New Roman', 30))
date_label.pack()

update()

window.mainloop()
