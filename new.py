import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import database
import categories as cat
import database
import boot

class New:

	def __init__(self, master: object, db: object, root: object):
		self.db = db
		self.root = root
		self.frame = ttk.Frame(master, padding=(6, 0, 6, 6))
		self.categories = cat.Categories(self.frame, True)
		self.pdf_path = tk.StringVar(value='NULL')

		# buttons
		self.pdf_btn = ttk.Button(
			self.frame,
			text='Select',
			command=self.pdf_cmd
		)
		self.add_btn = ttk.Button(
			self.frame,
			text='Add',
			command=self.add_cmd
		)
		self.reset_btn = ttk.Button(
			self.frame,
			text='Reset',
			command=self.categories.reset_cmd,
			style='TButton'
		)

		# labels
		self.pdf_lb = ttk.Label(
			self.frame,
			text='pdf',
			font=(cat.Categories.FONT, 14),
			padding=(0, 3, 3, 3)
		)

		self.configure()

	def configure(self):
		# configure the frame
		self.frame.grid(column=0, row=0, sticky=(tk.N, tk.E, tk.S, tk.W))
		self.frame.columnconfigure(5, weight=1)
		self.frame.rowconfigure(cat.Categories.MEAL_TIME_ROW, weight=1)
		self.frame.rowconfigure(cat.Categories.MEAT_ROW, weight=1)
		self.frame.rowconfigure(cat.Categories.RATING_ROW, weight=1)
		self.frame.rowconfigure(cat.Categories.TYPE_ROW, weight=1)
		self.frame.rowconfigure(cat.Categories.TIME_ROW, weight=1)

		#configure pdf widget
		self.pdf_btn.grid(column=6, row=1, sticky=(tk.E))
		self.pdf_lb.grid(column=5, row=1, sticky=(tk.E))

		# configure add button
		self.add_btn.grid(column=6, row=6, sticky=(tk.S, tk.E))

		# configure reset button
		self.reset_btn.grid(column=6, row=5, sticky=(tk.E, tk.S))

	def pdf_cmd(self):
		self.pdf_path.set(value=filedialog.askopenfilename())

	def add_cmd(self):
		if self.categories.meal_time_val.get() == 'Any' or \
			self.categories.meat_val.get() == 'Any' or \
			self.categories.type_val.get() == 'Any' or \
			self.categories.name_val.get() == '':
			messagebox.showerror(title='Error', message='Invalid Attribute')
			return
		
		self.db.update(self.categories.name_val.get(), self.categories.meal_time_val.get(),
			self.categories.meat_val.get(), self.categories.to_rating_val.get(),
			self.categories.type_val.get(), self.categories.time_val.get(),
			self.pdf_path.get())
