import airpy
import os
import simplejson as json
from bs4 import BeautifulSoup

try:
    FileNotFoundError
except:
    FileNotFoundError = IOError


def is_doc_installed(name):
    directory = airpy.data_directory + '/' + name
    if os.path.exists(directory):
        return True
    else:
        return False


def package_info(name, parameter):
    directory = airpy.data_directory + '/' + name
    try:
        with open(directory + '/' + name + '_airpy.json') as json_file:
            data = json.load(json_file)
        return data['info'][parameter]
    except FileNotFoundError:
        # return 'No Description'
        # Try to extract the description of the file from the html title.
        version_tag = ['latest']
        for tag in version_tag:
            fulldirname = directory + '/' + name + '-' + tag
        try:
            with open(fulldirname + '/' + 'index.html') as html:
                index = BeautifulSoup(html)
                return index.title.string
        except FileNotFoundError:
            return 'No Description'