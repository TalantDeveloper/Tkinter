from tkinter import *
from tkinter import colorchooser


def click():
    color = colorchooser.askcolor()
    if not color:
        color[1] = 'red'
        window.config(bg=color[1])
    window.config(bg=color[1])


window = Tk()
window.title('Tkinter project')
window.geometry('820x560')
button = Button(text='choose color', bg='#29f0aa', foreground='white', command=click)
button.pack()
window.mainloop()
