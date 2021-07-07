from tkinter import *
from tkinter import ttk
from notebook import *

class App:
	INIT_WIN_SIZE = '600x400'

	def __init__(self):
		# root setup
		self.root = Tk()
		self.root.geometry(App.INIT_WIN_SIZE)
		self.root.rowconfigure(0, weight=1)
		self.root.columnconfigure(0, weight=1)

		# create a notebook widget
		self.notebook = Notebook(self.root)

		# set mainloop
		self.root.mainloop()