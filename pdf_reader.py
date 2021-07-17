import os
import boot
import subprocess

def open_pdf(path: str):
	"""
	Opens the input pdf path on native reader.

	"""
	subprocess.run([boot.PDF_CMD, path])