import re
import subprocess
import airpy
import os

from airpy.install import airinstall
def airautopilot():
	installed = subprocess.check_output(['pip','list'])
	pattern = re.compile('([\w]+)\s\([\d]*\.?[\d]*\.[\d]*\)\\n')
	package = pattern.findall(installed.decode('utf-8').lower())
	for each_package in package:
		airinstall(each_package)
