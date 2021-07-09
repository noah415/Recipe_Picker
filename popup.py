import tkinter as tk
from tkinter import ttk
import categories as cat

class Popup:
	def __init__(self, meal: object):
		self.meal = meal
		self.window = tk.Toplevel()
		self.frame = ttk.Frame(self.window)
		self.categories = cat.Categories(self.frame, False, self.meal)
		self.disable_categories()

		self.configure()

	def configure(self):
		self.frame.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

	def destroy(self):
		self.window.destroy()

	def disable_categories(self):
		self.categories.meal_time['state'] = 'disabled'
		self.categories.meat['state'] = 'disabled'
		self.categories.rating_to['state'] = 'disabled'
		self.categories.type['state'] = 'disabled'
		self.categories.time['state'] = 'disabled'

	def enable_categories(self):
		self.categories.meal_time['state'] = 'enable'
		self.categories.meat['state'] = 'enable'
		self.categories.rating_to['state'] = 'enable'
		self.categories.type['state'] = 'enable'
		self.categories.time['state'] = 'enable'