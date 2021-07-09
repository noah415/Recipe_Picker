import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import categories as cat
import database
import os

class Popup:
	def __init__(self, meal: object, db: object):
		self.meal = meal
		self.db = db
		self.window = tk.Toplevel()
		self.frame = ttk.Frame(self.window)
		self.categories = cat.Categories(self.frame, False, self.meal)
		self.path = meal[6]
		if self.path != '':
			self.pdf_path = tk.StringVar(value=os.path.basename(self.path))
		self.pdf_path = tk.StringVar(value=self.path)

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
		self.pdf_btn = ttk.Button(
			self.frame,
			text='Select pdf',
			command=self.pdf_cmd
		)
		self.pdf_lb = ttk.Label(
			self.frame,
			textvariable=self.pdf_path
		)

		self.disable_categories()
		self.configure()

	def configure(self):
		self.frame.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

		self.edit_btn.grid(column=5, row=4)
		self.save_btn.grid(column=5, row=6)
		self.pdf_btn.grid(column=5, row=5)

		self.pdf_lb.grid(column=0, row=6, columnspan=4)

	def destroy(self):
		self.window.destroy()

	def disable_categories(self):
		self.categories.meal_time['state'] = 'disabled'
		self.categories.meat['state'] = 'disabled'
		self.categories.rating_to['state'] = 'disabled'
		self.categories.type['state'] = 'disabled'
		self.categories.time['state'] = 'disabled'
		self.pdf_btn['state'] = 'disabled'
		self.save_btn['state'] = 'disabled'

	def enable_categories(self):
		self.categories.meal_time['state'] = 'enable'
		self.categories.meat['state'] = 'enable'
		self.categories.rating_to['state'] = 'enable'
		self.categories.type['state'] = 'enable'
		self.categories.time['state'] = 'enable'
		self.pdf_btn['state'] = 'enable'
		self.save_btn['state'] = 'enable'

	def save_cmd(self):
		self.disable_categories()
		self.db.delete_meal(self.meal[0])
		self.db.update(self.meal[0], self.categories.meal_time_val.get(),
			self.categories.meat_val.get(), self.categories.to_rating_val.get(),
			self.categories.type_val.get(), self.categories.time_val.get(), self.path)

	def pdf_cmd(self):
		self.path = filedialog.askopenfilename()
		self.pdf_path.set(value=os.path.basename(self.path))
		self.pdf_btn['state'] = 'disabled'
		print('opened pdf', self.path)

