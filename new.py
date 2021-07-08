import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import database
import categories as cat
import database as db
import boot

class New:

	def __init__(self, master: object, db: object):
		self.db = db
		self.new_meal = [None, None, None, None, None, None, None]
		self.frame = ttk.Frame(master, padding=(6, 0, 6, 6))
		self.categories = cat.Categories(self.frame, True)

		# buttons
		self.pdf_btn = ttk.Button(
			self.frame,
			text='Select',
			command=self.pdf_cmd
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

	def pdf_cmd(self):
		self.new_meal[boot.PATH] = filedialog.askopenfilename()
		print(self.new_meal[boot.PATH])