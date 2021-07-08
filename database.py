import pandas as pd
import main

NEW_SAVE = False

class Database:
	def __init__(self, df: object, backup: object):
		"""
		@type df: pandas.DataFrame
		@type backup: pandas.DataFrame

		@rtype: void
		"""
		self.df = df
		self.backup = backup

	def update(self, meal: str, meal_time: str, 
		meat: str, rating: int, meal_type: str, time: int):
		"""
		@type name: str
		@type meal_time: str
		@type meat: str
		@type rating: int
		@type type: str
		@type time: int

		@rtype: void
		"""
		# if there is a change to the previous database version
		if NEW_SAVE:
			self.backup = self.df.copy(deep=True)

		NEW_SAVE = True

		row = [meal, meal_time, meat, rating, meal_type, time]
		self.df.loc[len(df.index)] = row

	def undo(self):
		if not NEW_SAVE:
			return
		
		NEW_SAVE = False

		self.df = self.backup.copy(deep=True)

	def delete_r(self, row: int):
		"""
		@type row: int
		"""
		if NEW_SAVE:
			self.backup = self.df.copy(deep=True)

		NEW_SAVE = True

		self.df.drop(
			labels=[row],
			axis=0,
			inplace=True
		)

	def delete_meal(self, meal: str):
		"""
		@type meal: str
		"""
		if NEW_SAVE:
			self.backup = self.df.copy(deep=True)

		NEW_SAVE = True

		self.df.drop(
			self.df[self.df['Meal'] != meal].index,
			axis=1,
			inplace=True
		)

	def csv_update(self):
		"""
		This is used for when the application is shutting down
		"""
		print(main.DATABASE_PATH)
		print(main.BACKUP_PATH)

		self.df.to_csv(main.DATABASE_PATH)
		self.backup.to_csv(main.BACKUP_PATH)