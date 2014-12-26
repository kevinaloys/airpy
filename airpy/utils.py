import airpy
import os

def is_doc_installed(name):
	directory = airpy.data_directory + '/' + name
	if os.path.exists(directory):
		return True
	else:
		return False