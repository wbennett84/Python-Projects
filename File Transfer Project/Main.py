
# import all needed modules

import tkinter
import xferFUNC
from tkinter import *



#Define the class

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

# Describe the nature of the window

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('Transfer New & Modified Files')
        self.master.config(bg='light gray')


# TEXT LABELS
# Sets up entry fields and places them in the grid

        self.sourceEntry = Entry(self.master,text='Source Folder: ', font=("Helvetica", 16), fg='black', bg='lightgray')
        self.sourceEntry.grid(row=0, column=0, padx=(30,0), pady=(30,0))

        self.destEntry = Entry(self.master,text='Destination Folder: ', font=("Helvetica", 16), fg='black', bg='lightgray')
        self.destEntry.grid(row=1, column=0, padx=(30,0), pady=(30,0))




#BUTTONS

 # This button calls a function which selects tht source folder

        self.btnSource = Button(self.master, text="Select Source", width=15, height=2, command=lambda:xferFUNC.find_Dir(self))
        self.btnSource.grid(row=2, column=0, padx=(0,0), pady=(30,0), sticky=NE)

 # This button calls a function which selected the destination folder

        self.btnDest = Button(self.master, text="Select Destination", width=15, height=2, command=lambda:xferFUNC.find_Dir2(self))
        self.btnDest.grid(row=2, column=1, padx=(0,90), pady=(30,0), sticky=NE)

 # This button is what the user clicks to sort the files

        self.btnSort = Button(self.master, text="Sort", width=15, height=2, command=lambda:xferFUNC.Sorting(self))
        self.btnSort.grid(row=2, column=2, padx=(0,90), pady=(30,0), sticky=NE)



#     def cancel(self):
#         self.master.destroy()



# This makes the program run if it's running its own file
# It instantiates Tk() and ParentWindow
# It keeps the program running with root.mainloop()

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
