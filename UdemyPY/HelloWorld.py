from Tkinter import * #use 'tkinter' if you're using python 3.x

root = Tk()
Label (root, text = "Hello World!").pack() # .pack is essential to display the text on the screen...
					   # ...Without which no text will be displayed
root.mainloop() # this creates infinite loop which prevents windows from getting closed by itself

