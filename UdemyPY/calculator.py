from Tkinter import * #used to create GUI

__metaclass__ = type
#main class for calculator
class application(Frame):
	#used to initialize an instance
	def __init__(self, master): 

		Frame.__init__(self, master) #(visit for the doc)https://docs.python.org/2.7/library/tkinter.html#the-window-manager
		self.task = ""
		self.UserIn = StringVar()
		self.grid()
		self.create_widgets()



	def create_widgets(self):
		self.user_input = Entry(self, bg = "#5bc8ac", bd = 10,
			insertwidth = 4, width = 24,
			font = ("Verdana", 20, "bold"), textvariable = self.UserIn,
					justify = RIGHT)
		self.user_input.grid(columnspan = 4)

		self.user_input.insert(0, "0")




		self.button1 = Button(self, bg = "#98dbc6", bd = 5,
						text = "7", padx = 35,  pady = 25, font =("Helvetica", 20, "bold"),
						command = lambda:self.buttonClick(7))
		self.button1.grid(row = 2, column = 0, sticky = W)


		self.button2 = Button(self, bg = "#98dbc6", bd = 5,
						text = "8", padx = 35, pady = 25, font = ("Helvetica", 20, "bold"),
						command = lambda:self.buttonClick(8))
		self.button2.grid(row = 2, column = 1, sticky = W)


		self.button3 = Button(self, bg = "#98dbc6", bd = 5,
						text = "9", padx = 35, pady = 25, font = ("Helvetica", 20, "bold"),
						command = lambda:self.buttonClick(9))
		self.button3.grid(row = 2, column = 2, sticky = W)


		self.button4 = Button(self, bg = "#98dbc6", bd = 5,
						text = "4", padx = 35, pady = 25, font = ("Helvetica", 20, "bold"),
						command = lambda:self.buttonClick(4))
		self.button4.grid(row = 3, column = 0, sticky = W)


		self.button5 = Button(self, bg = "#98dbc6", bd = 5,
						text = "5", padx = 35, pady = 25, font = ("Helvetica", 20, "bold"),
						command = lambda:self.buttonClick(5))
		self.button5.grid(row = 3, column = 1, sticky = W)


		self.button6 = Button(self, bg = "#98dbc6", bd = 5,
						text = "6", padx = 35, pady = 25, font = ("Helvetica", 20, "bold"),
						command = lambda:self.buttonClick(6))
		self.button6.grid(row = 3, column = 2, sticky = W)


		self.button7 = Button(self, bg = "#98dbc6", bd = 5,
						text = "1", padx = 35, pady = 25, font = ("Helvetica", 20, "bold"),
						command = lambda:self.buttonClick(1))
		self.button7.grid(row = 4, column = 0, sticky = W)


		self.button8 = Button(self, bg = "#98dbc6", bd = 5,
						text = "2", padx = 35, pady = 25, font = ("Helvetica", 20, "bold"),
						command = lambda:self.buttonClick(2))
		self.button8.grid(row = 4, column = 1, sticky = W)


		self.button9 = Button(self, bg = "#98dbc6", bd = 5,
						text = "3", padx = 35, pady = 25, font = ("Helvetica", 20, "bold"),
						command = lambda:self.buttonClick(3))
		self.button9.grid(row = 4, column = 2, sticky = W)


		self.button10 = Button(self, bg = "#98dbc6", bd = 5,
						text= "0", padx = 35, pady = 25, font = ("Helvetica", 20, "bold"),
						command = lambda:self.buttonClick(0))
		self.button10.grid(row = 5, column = 0, sticky = W)



		self.addbutton = Button(self, bg = "#98dbc6", bd = 5,
						text = "+", padx = 35, pady = 25, font = ("Helvetica", 20, "bold"),
						command = lambda:self.buttonClick("+"))
		self.addbutton.grid(row = 2, column = 3, sticky = W)

		self.subbutton = Button(self, bg = "#98dbc6", bd = 5,
						text = "-", padx = 35, pady = 25, font = ("Helvetica", 20, "bold"),
						command = lambda:self.buttonClick("-"))
		self.subbutton.grid(row = 3, column = 3, sticky= W)

		self.mulbutton = Button(self, bg = "#98dbc6", bd = 5,
						text = "*", padx = 35, pady = 25, font = ("Helvetica", 20, "bold"),
						command = lambda:self.buttonClick("*"))
		self.mulbutton.grid(row = 4, column = 3, sticky = W)

		self.divbutton = Button(self, bg = "#98dbc6", bd = 5,
						text = "/", padx = 35, pady = 25, font = ("Helvetica", 20, "bold"),
						command = lambda:self.buttonClick("/"))
		self.divbutton.grid(row = 5, column = 3, sticky = W)



		self.equalbutton = Button(self, bg = "#e6d72a", bd = 5,
							text = "=", padx = 95, pady = 25, font = ("Helvetica", 20, "bold"),
							command = self.calculateTask)
		self.equalbutton.grid(row = 5, column = 1, sticky = W, columnspan = 2)

		self.clearDisplay = Button(self, bg = "#e6d72a", bd = 5,
							text = "AC", width = 28, padx = 5, font = ("Helvetica", 20, "bold"),
							command = self.clearDisplay)
		self.clearDisplay.grid(row = 1, columnspan = 4, sticky = W)

	def buttonClick(self, number):
		self.task = str(self.task) + str(number)
		self.UserIn.set(self.task)

	def calculateTask(self):
		self.data = self.user_input.get()
		try:
			self.answer = eval(self.data)
			self.displayText(self.answer)
			self.task = self.answer

		except SyntexError as e:
			self.displayText("Invalid Syntax!")
			self.task = ""
		
	def displayText(self, value):
		self.user_input.delete(0, END)
		self.user_input.insert(0, value)

	def clearDisplay(self):
		self.task = ""
		self.user_input.delete(0, END)
		self.user_input.insert(0, "0")

# root of the application
calculator = Tk()

calculator.title("Calculator")
app = application(calculator)

# window cant be resized
calculator.resizable(width = False, height = False)

calculator.mainloop()