import click
import requests
import os
import shutil
from appdirs import user_data_dir
from airpy.install import airinstall
from airpy.list import airlist
from airpy.start import airstart
from airpy.remove import airremove
def main():
	@click.group()
	def airpy():
		pass

	@airpy.command()
	@click.argument('name')
	def install(name):
		"""Install offline doc of a Python module."""
		airinstall(name)
		
	@airpy.command()
	@click.argument('name')
	def start(name):
		"""Open the doc in a web browser."""
		airstart(name)

	@airpy.command()
	@click.argument('name')
	def remove(name):
		"""Remove an installed doc."""
		airremove(name)
	
	@airpy.command()
	@click.argument('name')
	def update(name):
		"""Fetch the latest updated doc."""
		pass

	@airpy.command()
	@click.argument('name')
	def search(name):
		"""Search for the doc of a Python module."""
		pass
	
	@airpy.command()
	def list():
		"""List installed docs."""
		airlist()

	@airpy.command()
	def info(name):
		"""Get Information on a particular doc"""

	airpy()

if __name__ == '__main__':
	main()