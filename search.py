from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random as rand
import categories as cat
import popup
import database

class Search:
	FONT = 'Ariel'

	BUTTONS_ROW = 6

	def __init__(self, master: object, db: object):
		# set results list
		self.db = db
		self.results_val = StringVar(value=[])
		self.popups = []

		# set frame
		self.frame = ttk.Frame(master, padding=(6, 0, 6, 6))

		# label
		self.results_lb = ttk.Label(
			self.frame,
			text='Results',
			font=(Search.FONT, 18),
			padding=(0, 3, 3, 6)
		)

		# configure the categories
		self.categories = cat.Categories(self.frame, False)

		# buttons
		self.random_btn = ttk.Button(
			self.frame,
			text='Random',
			command=self.categories.random_cmd,
			style='TButton'
		)
		self.reset_btn = ttk.Button(
			self.frame,
			text='Reset',
			command=self.categories.reset_cmd,
			style='TButton'
		)
		self.find_btn = ttk.Button(
			self.frame,
			text='Find',
			style='TButton',
			command=self.find_cmd
		)
		self.more_btn = ttk.Button(
			self.frame,
			text='More',
			style='TButton'
		)
		self.chooseforme_btn = ttk.Button(
			self.frame,
			text='Choose For Me'
		)

		# listbox
		self.results_lbox = Listbox(
			self.frame,
			height=11,
			listvariable=self.results_val,
			selectmode='multiple'
		)

		# scrollbar
		self.results_scbar = ttk.Scrollbar(
			self.frame,
			orient=VERTICAL,
			command=self.results_lbox.yview
		)

		# configure all the widgets
		self.configure()
		self.bind()

	def configure(self):
		# configure the frame
		self.frame.grid(column=0, row=0, sticky=(N, E, S, W))
		self.frame.columnconfigure(5, weight=1)
		self.frame.rowconfigure(cat.Categories.MEAL_TIME_ROW, weight=1)
		self.frame.rowconfigure(cat.Categories.MEAT_ROW, weight=1)
		self.frame.rowconfigure(cat.Categories.RATING_ROW, weight=1)
		self.frame.rowconfigure(cat.Categories.TYPE_ROW, weight=1)
		self.frame.rowconfigure(cat.Categories.TIME_ROW, weight=1)
		self.frame.rowconfigure(Search.BUTTONS_ROW, weight=1)

		# configure results widget
		self.results_lb.grid(column=5, row=0, columnspan=2, sticky=(N))
		self.results_lbox.grid(column=5, row=1, rowspan=5, columnspan=1, sticky=(N, E, W, S))
		self.results_lbox.configure(yscrollcommand=self.results_scbar.set)
		self.results_scbar.grid(column=7, row=1, rowspan=5, sticky=(N, W, S))
		# Colorize alternating lines of the listbox https://tkdocs.com/tutorial/morewidgets.html

		# configure buttons
		self.random_btn.grid(column=0, row=Search.BUTTONS_ROW, columnspan=2, sticky=(W, S))
		self.reset_btn.grid(column=4, row=Search.BUTTONS_ROW, columnspan=2, sticky=(W, S))
		self.find_btn.grid(column=2, row=Search.BUTTONS_ROW, columnspan=2, sticky=(W, S))
		self.chooseforme_btn.grid(column=5, row=Search.BUTTONS_ROW, sticky=(E, S))

	def bind(self):
		self.results_lbox.bind('<Double-1>', self.show_popup)

	def find_cmd(self):
		filter_list = []
		meal_time_val = self.categories.meal_time_val.get()
		meat_val = self.categories.meat.get()
		to_val = self.categories.to_rating_val.get()
		from_val = self.categories.from_rating_val.get()
		type_val = self.categories.type_val.get()
		time_val = self.categories.time_val.get()

		filter_list = [meal_time_val, meat_val, to_val, from_val, type_val, time_val]
		
		if (to_val != 'Any' or from_val != 'Any') and \
			(int(to_val) - int(from_val)) < 0:
			messagebox.showerror(title='Error', message='Invalid Rating Range')

		self.results_val.set(self.db.get_filtered_res(filter_list))

	def show_popup(self, *args):
		print('popup')
		for i in range(len(self.popups)):
			self.popups[i].destroy()
		self.popups = []

		print(len(self.popups))
		vals = self.db.get_rows(self.results_lbox.curselection())
		print(vals)

		for val in vals:
			self.popups.append(popup.Popup(val))
