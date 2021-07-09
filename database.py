import pandas as pd
import main
from tkinter import messagebox

class Database:
	def __init__(self, df: object, backup: object):
		"""
		@type df: pandas.DataFrame
		@type backup: pandas.DataFrame

		@rtype: void
		"""
		self.df = df
		self.backup = backup

		self.new_save = False

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
		self.new_save = True
		print(self.df.head())

		self.backup = self.df.copy(deep=True)


		row = [meal, meal_time, meat, rating, meal_type, time, path]
		self.df.loc[len(self.df.index)] = row

	def get_names(self):
		return self.df['Meal'].tolist()

	def get_rows(self, r_nums: object = None):
		rows = []

		if self.df.empty:
			print('Database is empty on query')
			return rows
		elif r_nums is None:
			return self.df.values.tolist()
		else:
			for num in r_nums:
				rows.append(self.df.iloc[num].tolist())

		return rows

	def undo(self):
		if not self.new_save:
			return
		
		self.new_save = False

		self.df = self.backup.copy(deep=True)
		self.df.reset_index(drop=True, inplace=True)
		print(self.df.index)

	def delete_r(self, rows: int):
		"""
		@type row: int

		@rtype: void
		"""
		self.new_save = True
		self.backup = self.df.copy(deep=True)

		self.df.drop(
			labels=rows,
			axis=0,
			inplace=True
		)

		self.df.reset_index(drop=True, inplace=True)

	def delete_meal(self, meal: str):
		"""
		@type meal: str

		@rtype: void
		"""
		self.new_save = True
		
		self.backup = self.df.copy(deep=True)

		self.df.drop(
			self.df[self.df['Meal'] != meal].index,
			axis=1,
			inplace=True
		)

	def upload(self, xlsx_path: str, col_names: object, name_table: object):
		"""
		@type xlsx_path: str

		@type col_names: list of str
		@type name_table: dictionary 

		@rtype: void
		"""
		self.new_save = True

		self.backup = self.df.copy(deep=True)

		try:
			new_df = pd.read_excel(xlsx_path, usecols=col_names)
		except Exception as e:
			messagebox.showerror(title='Error', message='Column Name Does Not Match.\n' + str(e))
			return

		for name in col_names:
			new_df = new_df.rename(columns={name: name_table[name]})
			print('renamed', name, 'to', name_table[name])
		
		self.df = pd.concat([self.df, new_df],
				axis=0,
				ignore_index=True		
		)

	def csv_update(self):
		"""
		This is used for when the application is shutting down

		@rtype: void
		"""
		if not self.new_save:
			print("Database: No changes were made to database")
			return
		try:
			self.df.to_csv(main.DATABASE_PATH, index=False)
		except Exception:
			print('Error: Shutdown failed to update most recent changes to path',
				main.DATABASE_PATH)
		try:
			self.backup.to_csv(main.BACKUP_PATH, index=False)
			print("Database: Application properly saved any recent session's changes")
		except Exception:
			print('Error: Shutdown failed to update backup changes to path', main.BACKUP_PATH)
