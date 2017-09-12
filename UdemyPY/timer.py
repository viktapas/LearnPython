from Tkinter import *
import ttk
import tkFont
import time
import datetime

global endTime

def quit(*args): 
	root.destroy() #exit the app

def cant_wait():
	#get the remaining time until the event
	timeLeft = endTime - datetime.datetime.now()
	#remove the microseconds left
	timeLeft = timeLeft - datetime.timedelta(microseconds = timeLeft.microseconds)

	#set timeLeft to txt
	txt.set(timeLeft)

	#trigger the countdown after 1000ms
	root.after(1000, cant_wait)

#create widget
root = Tk()
root.attributes("-fullscreen", False)
root.config(background = 'black')
root.bind('x', quit)
root.after(1000, cant_wait)

#set the end date and time for the countdown
endTime = datetime.datetime(2017,9,30, 0, 0) #first zero represents hours and minutes
											 #and second one represents seconds
# font style
fnt = tkFont.Font(family = 'Helvetica', size = 90, weight = 'bold')
txt = StringVar()
lbl = ttk.Label(root, textvariable = txt, font = fnt, foreground = 'white', background = 'black') #
# aligns the text to center
lbl.place(relx = 0.5, rely = 0.5, anchor = CENTER)
root.mainloop() #prevent app from close