import click
import airpy
import os
import webbrowser


def airstart(name):
	directory = airpy.data_directory + '/' + name
	if not os.path.exists(directory):
		click.echo('Docs for '+ name + ' is not installed.')
		click.echo('You can install it by typing, airpy install ' + name)
	else:
		static_dir = directory + '/' + name + '-latest' + '/index.html' 
		return webbrowser.open(static_dir)