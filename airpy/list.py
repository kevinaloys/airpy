import os
import airpy
def airlist():
	installed_docs = os.listdir(airpy.data_directory)
	for dir in installed_docs:
		print(dir, end= '  ')
	print(end = '\n')