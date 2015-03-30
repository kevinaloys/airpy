from __future__ import print_function
import os
import airpy
import simplejson as json
import click
import requests
from airpy import utils
from colorama import init
from colorama import Fore, Back, Style
init()


def airlist():
	installed_docs = os.listdir(airpy.data_directory)
	return installed_docs


def print_list():
	installed_docs = airlist()
	print(Fore.YELLOW + Style.BRIGHT + 'Python Project', end = ' '*20)
	print(Fore.YELLOW + Style.BRIGHT + 'Summary')
	print(Fore.WHITE + Style.DIM + '-'*14, end = ' ' * 11)
	print(Fore.WHITE + Style.DIM + '-'*24,)
	print()
	for dir in installed_docs:
		print(Fore.GREEN + Style.BRIGHT + dir + ' '*(25 - len(dir)) + Fore.WHITE + Style.NORMAL + utils.package_info(dir,'summary'))
	print(end = '\n')

