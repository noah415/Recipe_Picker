from tkinter import *
from tkinter import ttk
from app import *
from boot import boot
import pandas as pd

def main():
	# boot
	df = boot()

	# Run the app
	app = App(df)
	app.mainloop()

if __name__ == "__main__":
	main()