import airpy
from airpy import utils
import shutil

def airremove(name):
	for doc in name:
		remove(doc)


def remove(name):
	if utils.is_doc_installed(name):
		directory = airpy.data_directory + '/' + name
		shutil.rmtree(directory)
		return True
	else:
		return False