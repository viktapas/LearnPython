from Tkinter import * #Tkinter libarary used to create GUI application
#from Tkinter 
import ttk
import tkFont # import 'font' instead in python3
import time
import datetime

def quit(*args): 
    root.destroy()  #closes the window

def clock_time():
	time = datetime.datetime.now() #gets current time
	#time = (time.strftime("%H:%M:%S")) #time format
	time = (time.strftime("%d-%m-%y   %H:%M:%S")) #time woth date format

	txt.set(time)

	root.after(1000,clock_time)
 #these variables are for the window screen
 #creates widgets
root = Tk()
root.attributes("-fullscreen", False)
root.config(background = 'black') # use 'configure' instead in python3
root.bind("x", quit)
root.after(1000, clock_time)

#these variables are for the clock itself
fnt = tkFont.Font(family = 'Helvetics', size = 80, weight = 'bold')
txt = StringVar()
lbl = ttk.Label(root, textvariable = txt, font = fnt, foreground = "white", background = "black")
lbl.place(relx = 0.5, rely = 0.5, anchor = CENTER) #aling the clock to the center

root.mainloop()

    

