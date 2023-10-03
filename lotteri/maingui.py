from tkinter import *
from tkinter import messagebox
import lotteri

# create a root window 
root = Tk()
root.title("Lotteri")

# create listbox object
listbox = Listbox(root, height = 4
                  width = 30
                  bg = "white",
                  activestyle = 'DOTBOX'
                  font = "Helvetica"
                  fg = "blue")

# Define the size of the window 
root.geometry("380x380")

lotteriet = lotteri.Lotteri()

# create a label 
label_antal = Labal(root, text="Antal Lotter, max 3st :")
label_antal.grid(row=0, colume=0, sticky=E, padx=5, pady=5)

#create an input textbox
textbox_antal = Entry(root, width=2)
textbox_antal.grid(row=0, column=1, sticky=W, padx=5, pady=5)
textbox_antal.focus_set()