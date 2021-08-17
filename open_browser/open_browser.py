import webbrowser
from tkinter import *

root = Tk( )

root.title('Abrir Browser')
root.geometry('300x200')

def gooogle():
    webbrowser.open('www.google.com')

mygooogle = Button(root, text='Abrir o Google', command=google).pack(pady=20)
root.mainloop()