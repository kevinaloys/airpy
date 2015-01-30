import airpy
import os
import json

try:
	FileNotFoundError
except:
	FileNotFoundError = IOError

def is_doc_installed(name):
	directory = airpy.data_directory + '/' + name
	if os.path.exists(directory):
		return True
	else:
		return False

def package_info(name, parameter):
	directory = airpy.data_directory + '/' + name
	try:
		with open(directory + '/' + name + '_airpy.json') as json_file:
			data = json.load(json_file)
		return data['info'][parameter]
	except FileNotFoundError:
		return 'No Description'
