"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

#from setuptools import setup
from distutils.core import setup
import py2exe

APP = [{'script': 'main.py', 'icon_resources': [(0, '../../packaging/Win32/NE1.ico')]}]
DATA_FILES = []
OPTIONS = {'argv_emulation': True}

setup(
    windows=APP
    #app=APP,
    #name='NanoEngineer-1',
    #data_files=DATA_FILES,
    #options={'py2app': OPTIONS},
    #setup_requires=['py2app'],
)
