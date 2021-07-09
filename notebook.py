from tkinter import *
from tkinter import ttk
import search as s
import new
import data
import database

class Notebook:
	def __init__(self, root: object, db: object):
		"""
		@type root: tkinter.Tk
		@type db: Database object
		"""
		self.db = db
		self.root = root

		self.notebook = ttk.Notebook(self.root, padding=(0, 0, 0, 0))

		self.search = s.Search(self.notebook, self.db)
		self.database = data.Data(self.notebook, self.db)
		self.new = new.New(self.notebook, self.db, self.root)

		self.configure()

	def configure(self):
		self.notebook.grid(column=0, row=0, sticky=(N, E, W, S))

		self.notebook.add(self.search.frame, text="Search")
		self.notebook.add(self.database.frame, text="Database")
		self.notebook.add(self.new.frame, text="New")