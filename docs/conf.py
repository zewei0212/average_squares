import os, sys
sys.path.insert(0, os.path.abspath('..'))

project = 'Generating documentation with Sphinx'
copyright = '2025, Zewei Hou'
author = 'Zewei Hou'
release = 'n'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

