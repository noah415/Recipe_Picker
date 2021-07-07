from tkinter import *
from tkinter import ttk
import random as rand


class Search:
	FONT = 'Ariel'

	MEAL_TIME_VALS = ('Any', 'Breakfast', 'Brunch', 'Lunch', 'Dinner', 'Other')
	MEAL_TIME_ROW = 1

	MEAT_VALS = ('Any', 'Chicken', 'Pork', 'Beef', 'Fish/Seafood', 'Veggie', 'Other')
	MEAT_ROW = 2

	RATING_VALS = ('0', '1', '2', '3', '4', '5')
	RATING_ROW = 3
	
	TYPE_VALS = ('Any', 'Asian', 'Mexican', 'American', 'Italian', 'Other')
	TYPE_ROW = 4

	TIME_ROW = 5

	BUTTONS_ROW = 6

	RESULTS_LIST = ['Meal'] * 100

	def __init__(self, master: object):
		# spinbox value variables
		self.meal_time_val = StringVar(value='Any')
		self.meat_val = StringVar(value='Any')
		self.from_rating_val = StringVar(value='0')
		self.to_rating_val = StringVar(value='5')
		self.type_val = StringVar(value='Any')
		self.time_val = StringVar(value='Any')
		self.results_val = StringVar(value=Search.RESULTS_LIST)

		# set frame
		self.frame = ttk.Frame(master, padding=(6, 0, 6, 6))

		# all labels
		self.categories_lb = ttk.Label(
			self.frame, 
			text='Categories', 
			font=(Search.FONT, 18),
			padding=(0, 3, 3, 6)
		)
		self.meal_time_lb = ttk.Label(
			self.frame,
			text='Meal Time',
			font=(Search.FONT, 14),
			padding=(6, 5, 0, 5)
		)
		self.meat_lb = ttk.Label(
			self.frame,
			text='Meat',
			font=(Search.FONT, 14),
			padding=(6, 5, 0, 5)
		)
		self.rating_lb = ttk.Label(
			self.frame,
			text='Rating',
			font=(Search.FONT, 14),
			padding=(6, 0, 0, 0)
		)
		self.from_lb = ttk.Label(
			self.frame,
			text='From',
			font=(Search.FONT, 12),
			padding=(0, 0, 0, 0)
		)
		self.to_lb = ttk.Label(
			self.frame,
			text='To',
			font=(Search.FONT, 12),
			padding=(6, 0, 6, 0)
		)
		self.type_lb = ttk.Label(
			self.frame,
			text='Type',
			font=(Search.FONT, 14),
			padding=(6, 5, 0, 5)
		)
		self.time_lb = ttk.Label(
			self.frame,
			text='Time',
			font=(Search.FONT, 14),
			padding=(6, 5, 0, 5)
		)
		self.results_lb = ttk.Label(
			self.frame,
			text='Results',
			font=(Search.FONT, 18),
			padding=(0, 3, 3, 6)
		)

		# spinboxes
		self.meal_time = ttk.Spinbox(
			self.frame, 
			values=Search.MEAL_TIME_VALS, 
			textvariable=self.meal_time_val
		)
		self.meat = ttk.Spinbox(
			self.frame, 
			values=Search.MEAT_VALS, 
			textvariable=self.meat_val
		)
		self.rating_from = ttk.Spinbox(
			self.frame, 
			values=Search.RATING_VALS, 
			textvariable=self.from_rating_val,
			width=3
		)
		self.rating_to = ttk.Spinbox(
			self.frame, 
			values=Search.RATING_VALS,
			textvariable=self.to_rating_val,
			width=3
		)
		self.type = ttk.Spinbox(
			self.frame, 
			values=Search.TYPE_VALS, 
			textvariable=self.type_val
		)
		self.time = ttk.Spinbox(
			self.frame, 
			from_=5,
			to=180, 
			increment=5,
			textvariable=self.time_val
		)

		# buttons
		self.random_btn = ttk.Button(
			self.frame,
			text='Random',
			command=self.random_cmd,
			style='TButton'
		)
		self.reset_btn = ttk.Button(
			self.frame,
			text='Reset',
			command=self.reset_cmd,
			style='TButton'
		)
		self.find_btn = ttk.Button(
			self.frame,
			text='Find',
			style='TButton'
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
			listvariable=self.results_val
		)

		# scrollbar
		self.results_scbar = ttk.Scrollbar(
			self.frame,
			orient=VERTICAL,
			command=self.results_lbox.yview
		)

		# configure all the widgets
		self.configure()

	def configure(self):
		self.frame.grid(column=0, row=0, sticky=(N, E, S, W))
		self.frame.columnconfigure(5, weight=1)
		self.frame.rowconfigure(Search.MEAL_TIME_ROW, weight=1)
		self.frame.rowconfigure(Search.MEAT_ROW, weight=1)
		self.frame.rowconfigure(Search.RATING_ROW, weight=1)
		self.frame.rowconfigure(Search.TYPE_ROW, weight=1)
		self.frame.rowconfigure(Search.TIME_ROW, weight=1)
		self.frame.rowconfigure(Search.BUTTONS_ROW, weight=1)
		self.categories_lb.grid(column=0, row=0, columnspan=4, sticky=(N))

		# configure meal time widget
		self.meal_time.grid(column=0, row=Search.MEAL_TIME_ROW, columnspan=4, sticky=(W))
		self.meal_time_lb.grid(column=4, row=Search.MEAL_TIME_ROW, sticky=(W))
		self.meal_time.state(['readonly'])

		# configure meat widget
		self.meat.grid(column=0, row=Search.MEAT_ROW, columnspan=4, sticky=(W))
		self.meat_lb.grid(column=4, row=Search.MEAT_ROW, sticky=(W))
		self.meat.state(['readonly'])

		# configure the rating widget
		self.rating_lb.grid(column=4, row=Search.RATING_ROW, sticky=(W))
		self.from_lb.grid(column=0, row=Search.RATING_ROW, sticky=(W))
		self.to_lb.grid(column=2, row=Search.RATING_ROW, sticky=(W))
		self.rating_from.grid(column=1, row=Search.RATING_ROW, sticky=(E))
		self.rating_to.grid(column=3, row=Search.RATING_ROW, sticky=(E))
		self.rating_from.state(['readonly'])
		self.rating_to.state(['readonly'])

		# configure type widget
		self.type.grid(column=0, row=Search.TYPE_ROW, columnspan=4, sticky=(W))
		self.type_lb.grid(column=4, row=Search.TYPE_ROW, sticky=(W))
		self.type.state(['readonly'])

		# configure time widget
		self.time.grid(column=0, row=Search.TIME_ROW, columnspan=4, sticky=(W))
		self.time_lb.grid(column=4, row=Search.TIME_ROW, sticky=(W))

		# configure results widget
		self.results_lb.grid(column=5, row=0, columnspan=2, sticky=(N))
		self.results_lbox.grid(column=5, row=1, rowspan=5, columnspan=2, sticky=(N, E, W, S))
		self.results_lbox.configure(yscrollcommand=self.results_scbar.set)
		self.results_scbar.grid(column=7, row=1, rowspan=5, sticky=(N, W, S))
		# Colorize alternating lines of the listbox https://tkdocs.com/tutorial/morewidgets.html

		# configure buttons
		self.random_btn.grid(column=0, row=Search.BUTTONS_ROW, columnspan=2, sticky=(W, S))
		self.reset_btn.grid(column=2, row=Search.BUTTONS_ROW, columnspan=2, sticky=(W, S))
		self.find_btn.grid(column=4, row=Search.BUTTONS_ROW, sticky=(W, S))
		self.chooseforme_btn.grid(column=5, row=Search.BUTTONS_ROW, sticky=(S))
		self.more_btn.grid(column=6, row=Search.BUTTONS_ROW, sticky=(W, S))

	def reset_cmd(self):
		self.meal_time_val.set('Any')
		self.meat_val.set('Any')
		self.from_rating_val.set('0')
		self.to_rating_val.set('5')
		self.type_val.set('Any')
		self.time_val.set('Any')

	def random_cmd(self):
		rand.seed()
		mealtime_index = rand.randint(1, 4)
		meat_index = rand.randint(1, 5)
		type_index = rand.randint(1, 4)

		self.meal_time_val.set(Search.MEAL_TIME_VALS[mealtime_index])
		self.meat_val.set(Search.MEAT_VALS[meat_index])
		self.type_val.set(Search.TYPE_VALS[type_index])