from tkinter import *
from tkinter import ttk


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

	def __init__(self, master:object):
		# spinbox value variables
		self.meal_time_val = StringVar(value='Any')
		self.meat_val = StringVar(value='Any')
		self.from_rating_val = StringVar(value='0')
		self.to_rating_val = StringVar(value='5')
		self.type_val = StringVar(value='Any')
		self.time_val = StringVar(value='Any')

		# set frame
		self.frame = ttk.Frame(master, padding=(6, 0, 0, 0))

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
			text='Random'
		)
		self.reset_btn = ttk.Button(
			self.frame,
			text='Reset',
			command=self.reset_cmd
		)
		self.find_btn = ttk.Button(
			self.frame,
			text='Find'
		)
		self.more_btn = ttk.Button(
			self.frame,
			text='More'
		)

		# configure all the widgets
		self.configure()

	def configure(self):
		self.frame.grid(column=0, row=0, sticky=(N, E, S, W))
		self.frame.columnconfigure(5, weight=1)
		self.categories_lb.grid(column=0, row=0, columnspan=4, sticky=(N))

		# configure meat widget
		self.meat.grid(column=0, row=Search.MEAT_ROW, columnspan=4, sticky=(W))
		self.meat_lb.grid(column=4, row=Search.MEAT_ROW, sticky=(W))
		self.meat.state(['readonly'])

		# configure meal time widget
		self.meal_time.grid(column=0, row=Search.MEAL_TIME_ROW, columnspan=4, sticky=(W))
		self.meal_time_lb.grid(column=4, row=Search.MEAL_TIME_ROW, sticky=(W))
		self.meal_time.state(['readonly'])

		# configure the rating widget
		self.rating_lb.grid(column=4, row=Search.RATING_ROW, sticky=(W))
		self.from_lb.grid(column=0, row=Search.RATING_ROW, sticky=(W))
		self.to_lb.grid(column=2, row=Search.RATING_ROW, sticky=(W))
		self.rating_from.grid(column=1, row=Search.RATING_ROW, sticky=(E))
		self.rating_to.grid(column=3, row=Search.RATING_ROW, sticky=(E))
		self.rating_from.state(['readonly'])
		self.rating_to.state(['readonly'])

		#configure type widget
		self.type.grid(column=0, row=Search.TYPE_ROW, columnspan=4, sticky=(W))
		self.type_lb.grid(column=4, row=Search.TYPE_ROW, sticky=(W))
		self.type.state(['readonly'])

		#configure time widget
		self.time.grid(column=0, row=Search.TIME_ROW, columnspan=4, sticky=(W))
		self.time_lb.grid(column=4, row=Search.TIME_ROW, sticky=(W))

		# configure buttons
		self.random_btn.grid(column=0, row=Search.BUTTONS_ROW, columnspan=2, sticky=(W))
		self.reset_btn.grid(column=2, row=Search.BUTTONS_ROW, columnspan=2, sticky=(W))
		self.find_btn.grid(column=4, row=Search.BUTTONS_ROW, columnspan=2, sticky=(W))
		self.more_btn.grid(column=6, row=Search.BUTTONS_ROW, columnspan=2, sticky=(W))

	def reset_cmd(self):
		self.meal_time_val.set('Any')
		self.meat_val.set('Any')
		self.from_rating_val.set('0')
		self.to_rating_val.set('5')
		self.type_val.set('Any')
		self.time_val.set('Any')