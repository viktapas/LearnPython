#the output of this program will be in the terminal

import sys

from Tkinter import * #used for GUI

def timesTable():
	print "\n"
	for x in range(1, 11): #range from 1 to 10

		#assigning input from the user to variable m
		m = int(enterTable.get())
		#calculation
		print "\t\t", m, "x", x," = ", m*x
#root
multiply = Tk()
multiply.geometry("250x250+700+200")
multiply.title("Multiplication Table")

#string input variable
enterTable = StringVar()

label1 = Label(multiply, text = "Multiplication TimesTable", font = 30,fg = "black").grid(row = 1, column =6)
label1 = Label(multiply, text = "						").grid(row = 2, column = 6)
#setting GUI for input
entry5 = Entry(multiply, textvariable = enterTable, justify = "center").grid(row = 3, column = 6)
label1 = Label(multiply, text = "						").grid(row = 4, column = 6)


button1 = Button(multiply, text = "Times Table", command = timesTable).grid(row = 5, column = 6)
label1 = Label(multiply, text = "						").grid(row = 6, column = 6)
quit = Button(multiply, text = "Quit", fg = "red", command = multiply.destroy).grid(row = 7, column = 6)
multiply.mainloop()