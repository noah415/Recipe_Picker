import tkinter as tk
from tkinter import ttk
import database
import categories as cat
import popup

class Data:
	CUR_ROWS = []

	def __init__(self, master: object, db: object):
		self.frame = ttk.Frame(master, padding=(6, 6, 6, 6))
		self.db = db
		self.meals_vals = tk.StringVar()
		self.refresh()
		self.popup = None

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
			listvariable=self.meals_vals
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
		self.refresh_btn.grid(column=3, row=1, sticky=(tk.S))
		self.undo_btn.grid(column=3, row=2, sticky=(tk.S))
		self.delete_btn.grid(column=3, row=3, sticky=(tk.S))

		# configure database widget
		self.meals_lbox.grid(column=0, row=1, rowspan=4, sticky=(tk.N, tk.E, tk.W, tk.S))
		self.meals_lbox.configure(yscrollcommand=self.meals_scbar.set)
		self.meals_scbar.grid(column=1, row=1, rowspan=3, sticky=(tk.N, tk.W, tk.S))

	def bind(self):
		self.meals_lbox.bind('<Double-1>', self.show_popup)

	def upload_excel(self):
		print('upload')

	def refresh(self):
		print('im refreshing...')
		self.meals_vals.set(value=self.db.get_names())

	def conv_rowtostr(self):
		lst = self.db.get_rows()
		ret = []

		for row in lst:
			row = [str(i) for i in row]
			string = ',      '.join(row)
			ret.append(string)

		return ret

	def show_popup(self, *args):
		self.popup = popup.Popup([0])

	def delete(self):
		pass

	def undo(self):
		pass
