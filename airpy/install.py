import os
import requests
import zipfile
import click
import io
import airpy
import json

from airpy import utils

def airinstall(name):
	if utils.is_doc_installed(name):
		click.echo('Docs for ' + name + ' is already installed.')
	else:
		response = requests.get('https://readthedocs.org/projects/' + name + '/downloads/htmlzip/latest/')
		json_data = requests.get('https://pypi.python.org/pypi/'+ name + '/json').json()
		if response.status_code == 200:
			directory = airpy.data_directory + '/' + name
			os.makedirs(directory)
			z = zipfile.ZipFile(io.BytesIO(response.content), 'a')
			z.extractall(directory)
			with open(directory + '/' + name + '_airpy.json', 'w') as outfile:
				json.dump(json_data, outfile, sort_keys = True, indent = 4, ensure_ascii = False)
			return True
		else:
			click.echo('There are no docs for Python module named ' + '\'' + name + '\'')
			return False