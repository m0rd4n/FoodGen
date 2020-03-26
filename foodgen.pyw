from tkinter import *
from tkinter import messagebox

import htmlgen

window = Tk()
window.title("Foodgen")

window.geometry('350x150')
chk_state = BooleanVar()


def mondayCheck():
    if not chk_state.get():
        foodmonEntry.config(state='normal')
    else:
        foodmonEntry.config(state='disabled')


chk = Checkbutton(window, text='für Montag generieren?', var=chk_state, command=mondayCheck)
chk_state.set(True)

chk.grid(column=0, row=0)

foodmonLabel = Label(window, text="Was gibt es am Montag?  ")

foodmonEntry = Entry(window, width=16, state='disabled')

foodmonLabel.grid(column=0, row=1)
foodmonEntry.grid(column=1, row=1)


def generate():
    htmlgen.genhtml(foodmonEntry.get(), chk_state.get())
    messagebox.showinfo('Fertig', 'Der Essensplan wurde generiert')



genButton = Button(window, text="Generiere Plan", command=generate)
genButton.grid(row=2, pady=30)

window.mainloop()
