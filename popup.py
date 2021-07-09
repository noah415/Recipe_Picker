import tkinter as tk
from tkinter import ttk

class Popup:
	def __init__(self, meal: object):
		self.window = tk.Toplevel()

	def destroy(self):
		self.window.destroy()