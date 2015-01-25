from __future__ import print_function
import os
import airpy
import json
import click
import requests
from colorama import init
from colorama import Fore, Back, Style
init()


def airlist():
	installed_docs = os.listdir(airpy.data_directory)
	return installed_docs


def print_list():
	installed_docs = airlist()
	print(Fore.YELLOW + Style.BRIGHT + 'Python Project', end = '\t'*6)
	print(Fore.YELLOW + Style.BRIGHT + 'Summary')
	print(Fore.WHITE + Style.DIM + '-'*15, end = '\t' * 5)
	print(Fore.WHITE + Style.DIM + '-'*24,)
	print()
	for dir in installed_docs:
		print(Fore.GREEN + Style.BRIGHT + dir)
	print(end = '\n')

