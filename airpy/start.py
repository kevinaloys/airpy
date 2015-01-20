import click
import airpy
import os


def airstart(name):
	file_extensions = ['index.html','contents.html']
	directory = airpy.data_directory + '/' + name
	if not os.path.exists(directory):
		click.echo('Docs for '+ name + ' is not installed.')
		click.echo('You can install it by typing, airpy install ' + name)
	else:
		for each_extension in file_extensions:
			if os.path.exists(directory + '/' + name + '-latest' + '/' + each_extension):
				static_dir = directory + '/' + name + '-latest' + '/' + each_extension
		
		return click.launch(static_dir)