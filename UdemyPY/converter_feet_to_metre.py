from Tkinter import * #use tkinter in python3
import ttk

#logic/function for converting feet to meters
def calculate(*args):
	try:
		value = float(feet.get())
		meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
	except ValueError:
		pass


#root of the application
root = Tk()
root.title("Feet to Meters")

mainframe = ttk.Frame(root, padding = "3 3 12 12")
mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S))
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
 #variables
feet = StringVar()
meters = StringVar()
#widget
feet_entry = ttk.Entry(mainframe, width = 7, textvariable = feet)
feet_entry.grid(column = 2, row = 1, sticky =(W, E))
#create label
ttk.Label(mainframe, textvariable = meters).grid(column = 2, row = 2,
		sticky = (W, E))
#calculate button
ttk.Button(mainframe, text = "Calculate",
		command = calculate).grid(column =3 , row = 3, stick = W)
#create labels
ttk.Label(mainframe, text = "feet").grid(
		column = 3, row = 1, sticky = W)
ttk.Label(mainframe, text = "is equivalent to").grid(
		column = 1, row = 2, sticky = E)
ttk.Label(mainframe, text = "meters").grid(
		column = 3, row = 2, sticky = W)
#set padding to all child of mainframe
for child in mainframe.winfo_children(): child.grid_configure(
		padx = 5, pady = 5)
# focus to the widget feet_entry
feet_entry.focus()
#binds Return/Enter key and calculate. So, both do same work
root.bind("<Return>", calculate)

#keep app running until closed by the user
root.mainloop()