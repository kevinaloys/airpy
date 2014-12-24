import click
import requests
import os
import shutil
from appdirs import user_data_dir
from .install import airinstall
from .start import airstart
from .list import airlist

__author__ = 'Kevin Aloysius'
appname = 'airpy'
appauthor = __author__
data_directory = user_data_dir(appname, appauthor)

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
	
if __name__ == '__main__':
	airpy()