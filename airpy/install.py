import os
import requests
import zipfile
import click
import io
import airpy
import simplejson as json

from airpy import utils


def install_metadata(name):
	directory = airpy.data_directory + '/' + name
	metadata_response = requests.get('https://pypi.python.org/pypi/'+ name + '/json')
	if metadata_response.status_code == 200:
		metadata = metadata_response.json()
		if not os.path.exists(directory):
			os.makedirs(directory)
		with open(directory + '/' + name + '_airpy.json', 'w') as outfile:
			json.dump(metadata, outfile, sort_keys = True, indent = 4, ensure_ascii = False)
		return True
	else:
		return False


def install_documents(name):
	response = requests.get('https://readthedocs.org/projects/' + name + '/downloads/htmlzip/latest/')
	if response.status_code == 200:
		directory = airpy.data_directory + '/' + name
		if not os.path.exists(directory):
			os.makedirs(directory)
		z = zipfile.ZipFile(io.BytesIO(response.content), 'a')
		z.extractall(directory)
		return True
	else:
		return False


def airinstall(name):
    if utils.is_doc_installed(name):
        click.echo('Docs for ' + name + ' is already installed.')
    else:
        if install_documents(name):
            install_metadata(name)