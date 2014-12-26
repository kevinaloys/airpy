import os
import requests
import zipfile
import click
import io
import airpy

def airinstall(name):
	directory = airpy.data_directory + '/' + name
	if os.path.exists(directory):
		click.echo('Docs for ' + name + ' is already installed.')
	response = requests.get('https://readthedocs.org/projects/' + name + '/downloads/htmlzip/latest/')
	if response.status_code == 200:
		if not os.path.exists(directory):
			os.makedirs(directory)
		filename = directory + '/' + name +'_airpy.zip'
		z = zipfile.ZipFile(io.BytesIO(response.content), 'a')
		z.extractall(directory)
	else:
		click.echo('There are no docs for Python module named ' + '\'' + name + '\'')