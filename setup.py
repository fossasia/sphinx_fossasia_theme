from setuptools import setup
import os.path
import sys


setup(
    name = 'sphinx_fossasia_theme',
    version = '0.0.3',
    author = 'Ujjwal Bhardwaj',
    author_email = 'ujjwalb1996@gmail.com',
    url = 'https://github.com/fossasia/sphinx_fossasia_theme',
    license = 'GNU',
    description = 'A Sphinx theme specific to FOSSASIA\'s Projects',
    packages = ['sphinx_fossasia_theme'],
    include_package_data = True,
    entry_points = {
        'sphinx.html_themes': [
            'sphinx_fossasia_theme = sphinx_fossasia_theme'
        ],
        'sphinx_themes': [
            'path = sphinx_fossasia_theme:get_html_theme_path'
        ],
    },
    install_requires = ['sphinx>=1.3'],
  	platforms = 'any',
  	classifiers = [
    	"Framework :: Sphinx :: Extension",
    	"Framework :: Sphinx :: Theme",
    	"Intended Audience :: Developers",
    	"Operating System :: OS Independent",
    	"Topic :: Documentation :: Sphinx",
    	"Topic :: Software Development :: Documentation",
  	],
    long_description = open('README.rst').read(),
)
