import random as rand
import tkinter as tk
from tkinter import ttk

class Categories:
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

	def __init__(self, master: object, has_name: bool):
		"""
		@type master: tk object

		@type has_name: bool
		@param has_name: True if name box is displayed

		@rtype: void
		"""
		self.master = master
		self.has_name = has_name
		# spinbox value variables
		self.meal_time_val = tk.StringVar(value='Any')
		self.meat_val = tk.StringVar(value='Any')
		self.from_rating_val = tk.StringVar(value='0')
		self.to_rating_val = tk.StringVar(value='5')
		self.type_val = tk.StringVar(value='Any')
		self.time_val = tk.StringVar(value='Any')

		# all labels
		self.categories_lb = ttk.Label(
			self.master, 
			text='Categories', 
			font=(Categories.FONT, 18),
			padding=(0, 3, 3, 6)
		)
		self.meal_time_lb = ttk.Label(
			self.master,
			text='Meal Time',
			font=(Categories.FONT, 14),
			padding=(6, 5, 0, 5)
		)
		self.meat_lb = ttk.Label(
			self.master,
			text='Meat',
			font=(Categories.FONT, 14),
			padding=(6, 5, 0, 5)
		)
		self.rating_lb = ttk.Label(
			self.master,
			text='Rating',
			font=(Categories.FONT, 14),
			padding=(6, 0, 0, 0)
		)
		self.from_lb = ttk.Label(
			self.master,
			text='From',
			font=(Categories.FONT, 12),
			padding=(0, 0, 0, 0)
		)
		self.to_lb = ttk.Label(
			self.master,
			text='To',
			font=(Categories.FONT, 12),
			padding=(6, 0, 6, 0)
		)
		self.type_lb = ttk.Label(
			self.master,
			text='Type',
			font=(Categories.FONT, 14),
			padding=(6, 5, 0, 5)
		)
		self.time_lb = ttk.Label(
			self.master,
			text='Time',
			font=(Categories.FONT, 14),
			padding=(6, 5, 0, 5)
		)

		# spinboxes
		self.meal_time = ttk.Spinbox(
			self.master, 
			values=Categories.MEAL_TIME_VALS, 
			textvariable=self.meal_time_val
		)
		self.meat = ttk.Spinbox(
			self.master, 
			values=Categories.MEAT_VALS, 
			textvariable=self.meat_val
		)
		self.rating_from = ttk.Spinbox(
			self.master, 
			values=Categories.RATING_VALS, 
			textvariable=self.from_rating_val,
			width=3
		)
		self.rating_to = ttk.Spinbox(
			self.master, 
			values=Categories.RATING_VALS,
			textvariable=self.to_rating_val,
			width=3
		)
		self.type = ttk.Spinbox(
			self.master, 
			values=Categories.TYPE_VALS, 
			textvariable=self.type_val
		)
		self.time = ttk.Spinbox(
			self.master, 
			from_=5,
			to=180, 
			increment=5,
			textvariable=self.time_val
		)

		self.configure()

	def configure(self):
		self.categories_lb.grid(column=0, row=0, columnspan=4, sticky=(tk.N))

		# configure meal time widget
		self.meal_time.grid(column=0, row=Categories.MEAL_TIME_ROW, columnspan=4, sticky=(tk.W))
		self.meal_time_lb.grid(column=4, row=Categories.MEAL_TIME_ROW, sticky=(tk.W))
		self.meal_time.state(['readonly'])

		# configure meat widget
		self.meat.grid(column=0, row=Categories.MEAT_ROW, columnspan=4, sticky=(tk.W))
		self.meat_lb.grid(column=4, row=Categories.MEAT_ROW, sticky=(tk.W))
		self.meat.state(['readonly'])

		# configure the rating widget
		self.rating_lb.grid(column=4, row=Categories.RATING_ROW, sticky=(tk.W))
		self.from_lb.grid(column=0, row=Categories.RATING_ROW, sticky=(tk.W))
		self.to_lb.grid(column=2, row=Categories.RATING_ROW, sticky=(tk.W))
		self.rating_from.grid(column=1, row=Categories.RATING_ROW, sticky=(tk.E))
		self.rating_to.grid(column=3, row=Categories.RATING_ROW, sticky=(tk.E))
		self.rating_from.state(['readonly'])
		self.rating_to.state(['readonly'])

		# configure type widget
		self.type.grid(column=0, row=Categories.TYPE_ROW, columnspan=4, sticky=(tk.W))
		self.type_lb.grid(column=4, row=Categories.TYPE_ROW, sticky=(tk.W))
		self.type.state(['readonly'])

		# configure time widget
		self.time.grid(column=0, row=Categories.TIME_ROW, columnspan=4, sticky=(tk.W))
		self.time_lb.grid(column=4, row=Categories.TIME_ROW, sticky=(tk.W))

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

		self.meal_time_val.set(Categories.MEAL_TIME_VALS[mealtime_index])
		self.meat_val.set(Categories.MEAT_VALS[meat_index])
		self.type_val.set(Categories.TYPE_VALS[type_index])