import os
import pandas as pd
import csv
import sys
import database as db
import main

CSV_HEADER = ['Meal', 'Meal Time', 'Meat', 'Rating', 'Type', 'Time', 'Path']
NAME = 0
MEAL_TIME = 1
MEAT = 2
RATING = 3
TYPE = 4
TIME = 5
PATH = 6

def boot():
	"""
	@rtype: object
	@return: Returns a Database object
	"""
	# get Documents path: https://yagisanatode.com/2018/03/10/how-to-check-a-users-home-directory-for-a-folder-python-3/ 
	home = os.path.expanduser('~')
	doc_path = os.path.join(home, 'Documents')
	data_dir_path = os.path.join(doc_path, 'py_data')
	py_csv_path = os.path.join(data_dir_path, 'database.csv')
	py_csv_backup_path = os.path.join(data_dir_path, 'database_backup.csv')

	# configure the database folder
	check_dir(data_dir_path)

	# configure the database file
	check_file(py_csv_path)
	check_file(py_csv_backup_path)
	# set the static path variables
	main.DATABASE_PATH = py_csv_path
	main.BACKUP_PATH = py_csv_backup_path
	print("boot: set static variables in main, \n\tDATABASE_PATH:", 
		main.DATABASE_PATH, "\n\tBACKUP_PATH:", main.BACKUP_PATH)

	# create dataframe
	try:
		df = pd.read_csv(py_csv_path)
	except Exception:
		print("boot: Error: failed to open", main.DATABASE_PATH)
		sys.exit()
	try:
		backup = pd.read_csv(py_csv_backup_path)
	except Exception:
		print("boot: Error: failed to open", main.BACKUP_PATH)
		sys.exit()

	database = db.Database(df, backup)
	print("boot: Boot process successful")
	return database

def check_dir(dir_path: str):
	"""
	@type dir_path: str

	@rtype: void
	"""
	# check if app directory exists: https://www.geeksforgeeks.org/python-check-if-a-file-or-directory-exists-2/ 
	if not os.path.isdir(dir_path):
		print("check_dir: data directory does not exist", dir_path)
		try:
			os.mkdir(dir_path)
		except Exception:
			print("check_dir: Error: Failed to create directory", dir_path)
			sys.exit()
	else:
		print("check_dir: data directory exists")

def check_file(f_path: str):
	"""
	@type f_path: str
	
	@rtype: void
	"""
	# check if database csv file exists: https://www.geeksforgeeks.org/working-csv-files-python/ 
	if not os.path.isfile(f_path):
		print("check_file: data file does not exist", f_path)
		try:
			with open(f_path, 'w') as csvfile:
				writer = csv.writer(csvfile)
				writer.writerow(CSV_HEADER)
		except Exception:
			print("check_file: Error: Failed to create database file", f_path)
			sys.exit()
	else:
		print("check_file: data file exists")