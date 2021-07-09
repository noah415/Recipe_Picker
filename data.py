import tkinter as tk
from tkinter import ttk
import database
import categories as cat
import popup
import excel_popup as excel

class Data:
	CUR_ROWS = []

	def __init__(self, master: object, db: object):
		self.frame = ttk.Frame(master, padding=(6, 6, 6, 6))
		self.db = db
		self.meals_vals = tk.StringVar()
		self.refresh()
		self.popups = []
		self.excel_pop = None

		# buttons
		self.excel_upload_btn = ttk.Button(
			self.frame,
			text='Upload',
			command=self.upload_excel
		)
		self.refresh_btn = ttk.Button(
			self.frame,
			text='Refresh',
			command=self.refresh
		)
		self.delete_btn = ttk.Button(
			self.frame,
			text='Delete',
			command=self.delete
		)
		self.undo_btn = ttk.Button(
			self.frame,
			text='Undo',
			command=self.undo
		)
		self.open_btn = ttk.Button(
			self.frame,
			text='Open',
			command=self.show_popup
		)

		# labels
		self.meals_lb = ttk.Label(
			self.frame,
			text='Meals',
			font=(cat.Categories.FONT, 18),
			padding=(0, 3, 3, 3)
		)
		self.excel_lb = ttk.Label(
			self.frame,
			text='Excel',
			font=(cat.Categories.FONT, 14),
			padding=(10, 0, 3, 3)
		)

		# listbox
		self.meals_lbox = tk.Listbox(
			self.frame,
			height=11,
			listvariable=self.meals_vals,
			selectmode='multiple'
		)

		# scrollbar
		self.meals_scbar = ttk.Scrollbar(
			self.frame,
			orient=tk.VERTICAL,
			command=self.meals_lbox.yview
		)

		self.configure()
		self.bind()

	def configure(self):
		self.frame.grid(column=0, row=0, sticky=(tk.N, tk.E, tk.S, tk.W))
		self.frame.rowconfigure(1, weight=1)
		self.frame.columnconfigure(0, weight=1)
		# main label
		self.meals_lb.grid(column=0, row=0, sticky=(tk.N, tk.W))

		# configure excel widget
		self.excel_upload_btn.grid(column=3, row=0, sticky=(tk.N))
		self.excel_lb.grid(column=2, row=0, sticky=(tk.W))
		self.refresh_btn.grid(column=3, row=2, sticky=(tk.S))
		self.undo_btn.grid(column=3, row=3, sticky=(tk.S))
		self.delete_btn.grid(column=3, row=4, sticky=(tk.S))
		self.open_btn.grid(column=3, row=1, sticky=(tk.S))

		# configure database widget
		self.meals_lbox.grid(column=0, row=1, rowspan=5, sticky=(tk.N, tk.E, tk.W, tk.S))
		self.meals_lbox.configure(yscrollcommand=self.meals_scbar.set)
		self.meals_scbar.grid(column=1, row=1, rowspan=4, sticky=(tk.N, tk.W, tk.S))

	def bind(self):
		"""
		Configures all of the key and environment bindings
		"""
		self.meals_lbox.bind('<Double-1>', self.show_popup)

	def upload_excel(self):
		print('upload')
		self.excel_pop = excel.Excel_popup(self.db, self)

	def refresh(self):
		print('im refreshing...')
		self.meals_vals.set(value=self.db.get_names())

	def conv_rowtostr(self):
		"""
		grabs a list of lists of row attributes from database and 
		makes a list of row strings to return

		@rtype: list of strings
		"""
		lst = self.db.get_rows()
		ret = []

		for row in lst:
			row = [str(i) for i in row]
			string = ', '.join(row)
			ret.append(string)

		return ret

	def show_popup(self, *args):
		"""
		Used in the meals_lbox bind to mouse double click to show
		a meal's details. Calls the Popup class to create
		"""
		# check how many rows are selected and put that data in a list of lists
		for i in range(len(self.popups)):
			self.popups[i].destroy()
		self.popups = []

		print(len(self.popups))
		vals = self.db.get_rows(self.meals_lbox.curselection())
		print(vals)

		for val in vals:
			self.popups.append(popup.Popup(val))
			#disable the opend meals

	def delete(self):
		rows = self.meals_lbox.curselection()
		print('data: deleted rows:', list(rows))

		self.db.delete_r(list(rows))

		self.refresh()



	def undo(self):
		print("undo")
		self.db.undo()
		self.refresh()
