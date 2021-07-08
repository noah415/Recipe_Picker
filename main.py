from tkinter import *
from tkinter import ttk
from app import *
import boot
import database

DATABASE_PATH = ''
BACKUP_PATH = ''

def main():
	# boot
	db = boot.boot()

	# Run the app
	app = App(db)
	app.mainloop()
	db.csv_update()

if __name__ == "__main__":
	main()