# Import all needed modules

from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import time
import os
import shutil
import Main
from Main import *
import datetime
from datetime import timedelta








# This function centers the window in the screen

def center_window(self, w, h): # pass in the tkinter frame (master) reference and the w and h
    # get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo



# This function sets up a variable to store the dir the user selects
# for the source and it places the content of the variable as a string into the 
# entry field (sourceEntry)

def find_Dir(self):

    filepath = filedialog.askdirectory(initialdir="/")
    print(self.sourceEntry.insert(INSERT, filepath))


# This function sets up a variable to store the dir the user selects
# for the destination and it places the content of the variable as a string into the 
# entry field (destEntry)

def find_Dir2(self):
    
    self.filepath2 = filedialog.askdirectory(initialdir="/")
    print(self.destEntry.insert(INSERT, self.filepath2))


# This function sorts new and modified files from one folder 
# to another. If a file was modified or created less than 24 hours
# ago it will be moved

def Sorting(self):


#These two variables take the string value of the entry fields
# which have in them the directories the user selected

    sourceDir = self.sourceEntry.get()
    destDir = self.destEntry.get()

# This creates a list of the sourceDir folder, whatever is
# in the folder in terms of files
    src = os.listdir(sourceDir)

# This will iterate through the list just created
# and make a time comparison on the files and
# will move them if they are new or modified recently

    for fname in src:
        src_fname = os.path.join(sourceDir, fname)
        yesterdayTime = datetime.datetime.now() - timedelta(hours=24)
        modTime = os.path.getmtime(src_fname)
        dateTimeofFile = datetime.datetime.fromtimestamp(modTime)
        if yesterdayTime < dateTimeofFile:
            shutil.move(src_fname, destDir)



