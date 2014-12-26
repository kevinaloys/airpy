import airpy
from airpy import utils
import shutil

def airremove(name):
	if utils.is_doc_installed(name):
		directory = airpy.data_directory + '/' + name
		shutil.rmtree(directory)
