import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import boot
import database
import data

class Excel_popup:
	FONT = 'Ariel'

	MEAL_TIME_ROW = 1
	MEAT_ROW = 2
	RATING_ROW = 3
	TYPE_ROW = 4
	TIME_ROW = 5
	NAME_ROW = 6

	def __init__(self, db: object, data: object):
		self.db = db
		self.datawindow = data
		self.window = tk.Toplevel()
		self.frame = ttk.Frame(self.window)
		self.main_label = 'Excel Column Name'
		self.excel_path = ''
		self.is_selected = tk.StringVar(value='File Not Selected')
		self.name_table = {}
		self.col_names = []

		self.meal_time_val = tk.StringVar(value='')
		self.meat_val = tk.StringVar(value='')
		self.from_rating_val = tk.StringVar(value='')
		self.to_rating_val = tk.StringVar(value='')
		self.type_val = tk.StringVar(value='')
		self.time_val = tk.StringVar(value='')
		self.name_val = tk.StringVar(value='')
		self.sheet_val = tk.StringVar(value='')
		
		# all labels
		self.main_lb = ttk.Label(
			self.frame, 
			text=self.main_label, 
			font=(Excel_popup.FONT, 18),
			padding=(0, 3, 3, 6)
		)
		self.meal_time_lb = ttk.Label(
			self.frame,
			text='Meal Time',
			font=(Excel_popup.FONT, 14),
			padding=(6, 5, 10, 5)
		)
		self.meat_lb = ttk.Label(
			self.frame,
			text='Meat',
			font=(Excel_popup.FONT, 14),
			padding=(6, 5, 0, 5)
		)
		self.rating_lb = ttk.Label(
			self.frame,
			text='Rating',
			font=(Excel_popup.FONT, 14),
			padding=(6, 0, 0, 0)
		)
		self.type_lb = ttk.Label(
			self.frame,
			text='Type',
			font=(Excel_popup.FONT, 14),
			padding=(6, 5, 0, 5)
		)
		self.time_lb = ttk.Label(
			self.frame,
			text='Time',
			font=(Excel_popup.FONT, 14),
			padding=(6, 5, 0, 5)
		)
		self.name_lb = ttk.Label(
			self.frame,
			text='Meal Name',
			font=(Excel_popup.FONT, 14),
			padding=(6, 5, 0, 5)
		)
		self.select_lb = ttk.Label(
			self.frame,
			textvariable=self.is_selected,
			font=(Excel_popup.FONT, 10),
			padding=(6, 5, 0, 0)
		)
		self.sheet_lb = ttk.Label(
			self.frame,
			text='Sheet Number',
			font=(Excel_popup.FONT, 14),
			padding=(6, 5, 0, 5)
		)

		# buttons
		self.select_btn = ttk.Button(
			self.frame,
			text='Select File',
			command=self.select_cmd
		)
		self.upload_btn = ttk.Button(
			self.frame,
			text='Upload',
			command=self.upload_cmd
		)

		# entries
		self.meal_time = ttk.Entry(
			self.frame, 
			textvariable=self.meal_time_val
		)
		self.meat = ttk.Entry(
			self.frame, 
			textvariable=self.meat_val
		)
		self.rating = ttk.Entry(
			self.frame, 
			textvariable=self.to_rating_val
		)
		self.type = ttk.Entry(
			self.frame, 
			textvariable=self.type_val
		)
		self.time = ttk.Entry(
			self.frame, 
			textvariable=self.time_val
		)
		self.name = ttk.Entry(
			self.frame,
			textvariable=self.name_val
		)
		self.sheet = ttk.Entry(
			self.frame,
			textvariable=self.sheet_val
		)

		self.configure()


	def configure(self):
		self.frame.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
		self.main_lb.grid(column=0, row=0)
		self.name.grid(column=0, row=1)
		self.name_lb.grid(column=1, row=1)
		self.meal_time.grid(column=0, row=2)
		self.meal_time_lb.grid(column=1, row=2)
		self.meat.grid(column=0, row=3)
		self.meat_lb.grid(column=1, row=3)
		self.rating.grid(column=0, row=4)
		self.rating_lb.grid(column=1, row=4)
		self.type.grid(column=0, row=5)
		self.type_lb.grid(column=1, row=5)
		self.time.grid(column=0, row=6)
		self.time_lb.grid(column=1, row=6)
		self.select_btn.grid(column=2, row=5)
		self.select_lb.grid(column=2, row=4, sticky=(tk.S))
		self.upload_btn.grid(column=2, row=6)
		self.sheet.grid(column=0, row=7)
		self.sheet_lb.grid(column=1, row=7)

	def select_cmd(self):
		self.excel_path = filedialog.askopenfilename()
		self.select_btn['state'] = 'disabled'
		self.is_selected.set(value='File Selected')

	def upload_cmd(self):
		if not self.check_entries():
			self.select_btn['state'] = 'enabled'
			return

		inputs = [self.name.get(), self.meal_time.get(), self.meat.get(),
				self.rating.get(), self.type.get(), self.time.get()]

		for i in range(len(inputs)):
			if inputs[i] != '':
				self.name_table[inputs[i]] = boot.CSV_HEADER[i]
				self.col_names.append(inputs[i])

		self.db.upload(self.excel_path, self.col_names, self.name_table, int(self.sheet.get()))
		self.datawindow.refresh()
		self.window.destroy()


	def check_entries(self):
		if self.name.get() == '' or self.excel_path == '' or self.sheet_val.get() == '':
			messagebox.showerror(title='Error', message='Invalid Attribute')
			return False
		return True
