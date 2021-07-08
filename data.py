import tkinter as tk
from tkinter import ttk
import database
import categories as cat

class Data:
	CUR_ROWS = []

	def __init__(self, master: object, db: object):
		self.frame = ttk.Frame(master, padding=(6, 6, 6, 6))
		self.db = db
		Data.CUR_ROWS = self.meals_vals = self.db.get_rows()

		self.meals_val = tk.StringVar(value=self.meals_vals)

		# buttons
		self.excel_upload_btn = ttk.Button(
			self.frame,
			text='Upload',
			command=self.upload_excel()
		)

		# labels
		self.meals_lb = ttk.Label(
			self.frame,
			text='Meals',
			font=(cat.Categories.FONT, 18),
			padding=(0, 3, 3, 3)
		)

		# listbox
		self.meals_lbox = tk.Listbox(
			self.frame,
			height=11,
			listvariable=self.meals_val
		)

		# scrollbar
		self.meals_scbar = ttk.Scrollbar(
			self.frame,
			orient=tk.VERTICAL,
			command=self.meals_lbox.yview
		)

		self.configure()

	def configure(self):
		self.frame.grid(column=0, row=0, sticky=(tk.N, tk.E, tk.S, tk.W))
		self.frame.rowconfigure(1, weight=1)
		self.frame.columnconfigure(0, weight=1)
		# main label
		self.meals_lb.grid(column=0, row=0, sticky=(tk.N, tk.W))

		# configure excel widget
		self.excel_upload_btn.grid(column=2, row=0, sticky=(tk.N, tk.W))

		# configure results widget
		self.meals_lbox.grid(column=0, row=1, rowspan=3, sticky=(tk.N, tk.E, tk.W, tk.S))
		self.meals_lbox.configure(yscrollcommand=self.meals_scbar.set)
		self.meals_scbar.grid(column=1, row=1, rowspan=3, sticky=(tk.N, tk.W, tk.S))

	def upload_excel(self):
		pass
