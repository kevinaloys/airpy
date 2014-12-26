from setuptools import setup

setup (
	name = 'airpy',
	version = '0.0.1',
	description = 'Offline Documentation Installer for the Pythonic Soul',
	url = 'https://github.com/kevinaloys/airpy',
	author = 'Kevin Aloysius',
	author_email = 'kevinaloysius25@gmail.com',
	packages = ['airpy'],
	license = "MIT",
	install_requires = ['click','requests','appdirs'],
	entry_points='''
		[console_scripts]
		airpy = airpy.main:main
	''',

	)
