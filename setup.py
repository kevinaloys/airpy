from setuptools import setup

setup (
	name = 'airpy',
	version = '0.0.6',
	description = 'Documentation Installer for the Pythonic Soul',
	url = 'https://github.com/kevinaloys/airpy',
	author = 'Kevin Aloysius',
	author_email = 'kevinaloysius25@gmail.com',
	packages = ['airpy'],
	license = "MIT",
	install_requires = ['click','requests','appdirs','colorama'],
	classifiers = [
		'Development Status :: 1 - Planning',
		'Environment :: Console',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Natural Language :: English',
		'Programming Language :: Python :: 3.4',
		'Topic :: Documentation',
		],
	entry_points='''
		[console_scripts]
		airpy = airpy.main:main
	''',

	)
