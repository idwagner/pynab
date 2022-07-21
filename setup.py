
from setuptools import setup, find_packages
from subprocess import Popen, PIPE
import os
import re



PACKAGE = 'pynab'
AUTHOR = 'Isaac Wagner'
URL = 'https://github.com/idwagner/pynab'

ROOT = os.path.dirname(__file__)
VERSION='0.1.3'

def file_lines(filename):
    with open(filename, 'r') as fdesc:
        data = fdesc.read()
    return data.split("\n")


setup(
    # Basic info
    name=PACKAGE,
    version=VERSION,
    author=AUTHOR,
    url=URL,

    # Packages and depencies
    packages=find_packages(exclude=['tests*']),
    install_requires=[
        'certifi >= 14.05.14',
        'future; python_version<="2.7"',
        'six >= 1.10',
        'python_dateutil >= 2.5.3',
        'setuptools >= 21.0.0',
        'urllib3 >= 1.15.1',
        'click >= 7.1.2',
        'tabulate >= 0.8.7',
        'colorama >= 0.4.3',
    ],

    # Data files
    package_data={
        PACKAGE : [
            'templates/*.*',
            'templates/license/*.*',
            'templates/docs/*.*',
            'templates/package/*.*'
        ],
    },

    # Scripts
    entry_points={
        'console_scripts': [
            'ynab = pynab.cli:main'
        ],
    },
)
