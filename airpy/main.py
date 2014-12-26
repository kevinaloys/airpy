import click
import requests
import os
import shutil
from appdirs import user_data_dir
from airpy.install import airinstall
from airpy.list import airlist
from airpy.start import airstart
from airpy.remove import airremove
from airpy.autopilot import airautopilot
def main():
	@click.group()
	def airpy():
		"""AirPy : Documentation Installer for the Pythonic Soul™"""
		pass

	@airpy.command(help = 'Install offline doc of a Python module.')
	@click.argument('name')
	def install(name):
		airinstall(name)
		
	@airpy.command(help = 'Start a doc in a browser.')
	@click.argument('name')
	def start(name):
		airstart(name)

	@airpy.command(help = 'Remove an installed doc.')
	@click.argument('name')
	@click.option('--all')
	def remove(name, all):
		airremove(name)
	
	@airpy.command(help = 'Search for Python docs.')
	@click.argument('name')
	def search(name):
		pass
	
	@airpy.command(help = 'List installed docs.')
	def list():
		airlist()

	@airpy.command(help = 'Show information about installed docs.')
	@click.argument('name')
	def show(name):
		pass

	@airpy.command(help = 'Auto install docs.')
	def autopilot():
		airautopilot()

	airpy()

if __name__ == '__main__':
	main()