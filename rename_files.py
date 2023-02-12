# Libraries
import os
from tkinter import *


# Color variables
grayColor = "#cacaca"
whiteColor = "#fcfaf1"
yellowColor = "#e6b31e"
blackColor = "#343434"

# Window
win1 = Tk()
win1.title("Rename Files")
win1.geometry("1100x500")
win1.resizable(width=False, 
               height=False)
win1.config(bg=whiteColor)

# Image
img = PhotoImage(file="rename_files.png")

# Labels
lab0 = Label(win1,
             width=20,
             text="Rename Files\n Program",
             bg=grayColor,
             fg=blackColor,
             font="Ubuntu")
lab0.grid(row=0, 
          column=1, 
          ipadx=5, 
          ipady=5, 
          padx=20, 
          pady=10)

lab1 = Label(win1, 
             image=img,
             bg=whiteColor)
lab1.grid(row=0, 
         column=2)

lab2 = Label(win1, 
             width=20, 
             text="Directory", 
             bg=grayColor, 
             fg=blackColor, 
             font="Ubuntu")
lab2.grid(row=1, 
          column=1, 
          ipadx=5, 
          ipady=5, 
          padx=20, 
          pady=10)

lab3 = Label(win1, 
             width=20, 
             text="New name for files", 
             bg=grayColor, 
             fg=blackColor, 
             font="Ubuntu")
lab3.grid(row=2, 
          column=1, 
          ipadx=5, 
          ipady=5, 
          padx=20, 
          pady=10)

lab4 = Label(win1, 
             width=20, 
             text="Give the file extension\n (e.g. .txt, .jpg)", 
             bg=grayColor, 
             fg=blackColor, 
             font="Ubuntu")
lab4.grid(row=3, 
          column=1, 
          ipadx=5, 
          ipady=5, 
          padx=20, 
          pady=10)

lab5 = Label(win1, 
             width=55, 
             bg=grayColor, 
             fg=blackColor, 
             font="Ubuntu")
lab5.grid(row=4, 
          column=2, 
          ipadx=5, 
          ipady=5, 
          padx=20, 
          pady=10)

# Entries
ent1 = Entry(win1, 
             width=60, 
             bg=grayColor, 
             fg=blackColor, 
             font="Ubuntu")
ent1.grid(row=1, 
          column=2, 
          ipadx=5, 
          ipady=5, 
          padx=20, 
          pady=10)

ent2 = Entry(win1, 
             width=60, 
             bg=grayColor, 
             fg=blackColor, 
             font="Ubuntu")
ent2.grid(row=2, 
          column=2, 
          ipadx=5, 
          ipady=5, 
          padx=20, 
          pady=10)

ent3 = Entry(win1, 
             width=60, 
             bg=grayColor, 
             fg=blackColor, 
             font="Ubuntu")
ent3.grid(row=3, 
          column=2, 
          ipadx=5, 
          ipady=5, 
          padx=20, 
          pady=10)

# Function (Getting entries)
def renameFiles():
    # Renaming files on a masive way
    location = ent1.get()
    content = os.listdir(location)
    newName = ent2.get()
    fileExtension = ent3.get()
    sequence = 1
    
    for i in content:
        completeNewName = newName + "-" + str(sequence) + fileExtension
        lastFile = os.path.join(location, i)  
        newFile = os.path.join(location, completeNewName)
        os.rename(lastFile, newFile)
        sequence += 1

    lab5.configure(text="The files were rename correctly.")
    
# Button
btn = Button(win1, 
             width=20, 
             text="Execute", 
             bg=yellowColor, 
             fg=blackColor, 
             font="Ubuntu", 
             command=renameFiles)
btn.grid(row=4, 
         column=1, 
         ipadx=5, 
         ipady=5, 
         padx=20, 
         pady=10)
    

win1.mainloop()