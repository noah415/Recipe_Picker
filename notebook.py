from tkinter import *
from tkinter import ttk
import search as s
import new
import database

class Notebook:
	def __init__(self, root: object, db: object):
		"""
		@type root: tkinter.Tk
		@type db: Database object
		"""
		self.db = db

		self.notebook = ttk.Notebook(root, padding=(0, 0, 0, 0))

		self.search = s.Search(self.notebook)
		self.database = ttk.Frame(self.notebook)
		self.new = new.New(self.notebook, self.db)

		self.configure()

	def configure(self):
		self.notebook.grid(column=0, row=0, sticky=(N, E, W, S))

		self.database.grid(column=0, row=0, sticky=(N, E, S, W))

		self.notebook.add(self.search.frame, text="Search")
		self.notebook.add(self.database, text="Database")
		self.notebook.add(self.new.frame, text="New")