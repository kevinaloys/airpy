import re
import subprocess
import airpy
import os
from airpy.install import airinstall

def airautopilot():
	installed = subprocess.check_output(['pip','list'])
	pattern = re.compile('([\w]+)\s\([\d]*\.?[\d]*\.[\d]*\)\\n')
<<<<<<< HEAD
	package = pattern.findall(installed.decode('utf-8').lower())
=======
	package = pattern.findall(installed.decode('utf-8'))
>>>>>>> master
	for each_package in package:
		airinstall(each_package)
