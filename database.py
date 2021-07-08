import pandas as pd
import main

NEW_SAVE = False
IS_EMPTY = True

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
		meat: str, rating: int, meal_type: str, time: int, path: str):
		"""
		@type name: str
		@type meal_time: str
		@type meat: str
		@type rating: int
		@type type: str
		@type time: int
		@type path: str

		@rtype: void
		"""
		# if there is a change to the previous database version
		if NEW_SAVE:
			self.backup = self.df.copy(deep=True)

		NEW_SAVE = True

		row = [meal, meal_time, meat, rating, meal_type, time, path]
		self.df.loc[len(df.index)] = row

	def get_rows(self):
		rows = []

		if IS_EMPTY:
			return rows

	def undo(self):
		if not NEW_SAVE:
			return
		
		NEW_SAVE = False

		self.df = self.backup.copy(deep=True)

	def delete_r(self, row: int):
		"""
		@type row: int

		@rtype: void
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

		@rtype: void
		"""
		if NEW_SAVE:
			self.backup = self.df.copy(deep=True)

		NEW_SAVE = True

		self.df.drop(
			self.df[self.df['Meal'] != meal].index,
			axis=1,
			inplace=True
		)

	def upload(self, xlsx_path: str):
		"""
		@type xlsx_path: str

		@rtype: void
		"""
		if NEW_SAVE:
			self.backup = self.df.copy(deep=True)

		NEW_SAVE = True

		new_df = pd.read_excel(xlsx_path)

		self.df = pd.concat([self.df, new_df],
				axis=0,
				ignore_index=True		
		)

	def csv_update(self):
		"""
		This is used for when the application is shutting down

		@rtype: void
		"""
		try:
			self.df.to_csv(main.DATABASE_PATH)
		except Exception:
			print('Error: Shutdown failed to update most recent changes to path',
				main.DATABASE_PATH)
		try:
			self.backup.to_csv(main.BACKUP_PATH)
			print("Application properly saved any recent session's changes")
		except Exception:
			print('Error: Shutdown failed to update backup changes to path', main.BACKUP_PATH)
