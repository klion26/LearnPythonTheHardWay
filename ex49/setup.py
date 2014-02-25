try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
		'description': 'My Project',
		'author': 'klion26',
		'url': 'http://www.klion26.com',
		'download_url': 'where to download it.',
		'author_email': 'qcx978132955@gmail.com',
		'version': '0.1',
		'install_requires': ['nose'],
		'packages': ['ex47'],
		'scripts': [],
		'name': 'projectname'
		}

setup(**config)
