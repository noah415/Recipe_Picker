from tkinter import *
from tkinter import ttk
from search import *
import pandas as pd

class Notebook:
	def __init__(self, root:object):
		self.notebook = ttk.Notebook(root, padding=(0, 0, 0, 0))

		self.search = Search(self.notebook)
		self.database = ttk.Frame(self.notebook)
		self.new = ttk.Frame(self.notebook)

		self.configure()

	def configure(self):
		self.notebook.grid(column=0, row=0, sticky=(N, E, W, S))

		self.database.grid(column=0, row=0, sticky=(N, E, S, W))
		self.new.grid(column=0, row=0, sticky=(N, E, S, W))

		self.notebook.add(self.search.frame, text="Search")
		self.notebook.add(self.database, text="Database")
		self.notebook.add(self.new, text="New")