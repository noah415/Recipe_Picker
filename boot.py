import os
import pandas as pd
import csv
import sys
import database as db
import main

CSV_HEADER = ['Meal', 'Meal Time', 'Meat', 'Rating', 'Type', 'Time']

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

	print(main.DATABASE_PATH)
	print(main.BACKUP_PATH)
		
	# create dataframe
	try:
		df = pd.read_csv(py_csv_path)
		backup = pd.read_csv(py_csv_backup_path)
	except Exception:
		print("Error: failed to make a DataFrame")
		sys.exit()

	database = db.Database(df, backup)
	return database

def check_dir(dir_path: str):
	"""
	@type dir_path: str

	@rtype: void
	"""
	# check if app directory exists: https://www.geeksforgeeks.org/python-check-if-a-file-or-directory-exists-2/ 
	if not os.path.isdir(dir_path):
		print("data directory does not exist")
		os.mkdir(dir_path)
	else:
		print("data directory exists")

def check_file(f_path: str):
	"""
	@type f_path: str
	
	@rtype: void
	"""
	# check if database csv file exists: https://www.geeksforgeeks.org/working-csv-files-python/ 
	if not os.path.isfile(f_path):
		print("data file does not exist")
		try:
			with open(f_path, 'w') as csvfile:
				writer = csv.writer(csvfile)
				writer.writerow(CSV_HEADER)
		except Exception:
			print("Error: Failed to create database file")
			sys.exit()
	else:
		print("data file exists")