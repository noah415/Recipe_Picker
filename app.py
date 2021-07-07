from tkinter import *
from tkinter import ttk
from notebook import *

class App(Tk):
	INIT_WIN_SIZE = '590x300'

	def __init__(self):
		super().__init__()

		# root setup
		self.title('App')
		self.geometry(App.INIT_WIN_SIZE)
		self.rowconfigure(0, weight=1)
		self.columnconfigure(0, weight=1)
		self.minsize(550, 300)

		# create a notebook widget
		self.notebook = Notebook(self)