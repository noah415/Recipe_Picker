import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import categories as cat
import database
import os
import pdf_reader as pdf

class Popup:
	def __init__(self, meal: object, db: object):
		self.meal = meal
		self.db = db
		self.window = tk.Toplevel()
		self.frame = ttk.Frame(self.window)
		self.categories = cat.Categories(self.frame, False, self.meal)
		self.path = meal[6]
		""" 		if not self.path is None or self.path != '':
			self.pdf_path = tk.StringVar(value=os.path.basename(self.path))"""
		self.pdf_path = tk.StringVar(value=self.path)
		try:
			self.pdf_base_path = tk.StringVar(value=os.path.basename(self.path))
		except Exception:
			self.pdf_base_path = tk.StringVar(value='Empty')

		self.txt_box = tk.Text(
			self.frame,
			width=80,
			height=30
		)

		# buttons
		self.edit_btn = ttk.Button(
			self.frame,
			text='Edit',
			command=self.enable_categories
		)
		self.save_btn = ttk.Button(
			self.frame,
			text='Save',
			command=self.save_cmd
		)
		self.pdf_select_btn = ttk.Button(
			self.frame,
			text='Select PDF',
			command=self.pdf_cmd
		)
		self.pdf_val_lb = ttk.Label(
			self.frame,
			textvariable=self.pdf_base_path,
			width=20,
			padding=(0, 0, 6, 0)
		)
		self.pdf_open_btn = ttk.Button(
			self.frame,
			command=self.open_pdf,
			text='Open PDF'
		)

		self.disable_categories()
		self.configure()

	def configure(self):
		self.frame.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

		self.edit_btn.grid(column=5, row=0, sticky=(tk.W, tk.E))
		self.pdf_select_btn.grid(column=5, row=1)
		self.save_btn.grid(column=5, row=2, sticky=(tk.W, tk.E))

		self.pdf_val_lb.grid(column=0, row=6, columnspan=4)
		self.pdf_open_btn.grid(column=4, row=6)

	def destroy(self):
		self.window.destroy()

	def disable_categories(self):
		self.categories.meal_time['state'] = 'disabled'
		self.categories.meat['state'] = 'disabled'
		self.categories.rating_to['state'] = 'disabled'
		self.categories.type['state'] = 'disabled'
		self.categories.time['state'] = 'disabled'
		self.pdf_select_btn['state'] = 'disabled'
		self.save_btn['state'] = 'disabled'

	def enable_categories(self):
		self.categories.meal_time['state'] = 'enable'
		self.categories.meat['state'] = 'enable'
		self.categories.rating_to['state'] = 'enable'
		self.categories.type['state'] = 'enable'
		self.categories.time['state'] = 'enable'
		self.pdf_select_btn['state'] = 'enable'
		self.save_btn['state'] = 'enable'

	def save_cmd(self):
		self.disable_categories()
		self.db.delete_meal(self.meal[0])
		self.db.update(self.meal[0], self.categories.meal_time_val.get(),
			self.categories.meat_val.get(), self.categories.to_rating_val.get(),
			self.categories.type_val.get(), self.categories.time_val.get(), self.path)

	def pdf_cmd(self):
		self.path = filedialog.askopenfilename()
		self.pdf_path.set(value=self.path)
		self.pdf_select_btn['state'] = 'disabled'
	
	def open_pdf(self):
		if self.pdf_base_path != 'Empty':
			pdf.open_pdf(self.path)
			print('opened pdf', self.path)

