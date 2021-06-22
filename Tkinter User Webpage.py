#Import the required Libraries
from tkinter import *
from tkinter import ttk
import webbrowser
#Create an instance of Tkinter frame
win= Tk()
#Set the geometry of Tkinter frame
win.geometry("750x250")



#Create an Entry widget to accept User Input
source = StringVar()

entry= Entry(win, width= 40, textvariable=source)
entry.pack(pady=50)




# Create a function that creates a web page and inputs the 
# user-provided text, and then opens it in a new tab of the browser
def display_text():
       
   text = source.get()
   message = "<html><head></head><body><h1>%s</h1></body</html>" % text
   f = open("demofile.html", 'w')
   f.write(message)
   f.close()

   webbrowser.open_new_tab("demofile.html")



#Create a button to submit the user information
ttk.Button(win, text= "Create your own web page!",width= 30, command= display_text).pack(pady=20)

# Keeps the program running
win.mainloop()












