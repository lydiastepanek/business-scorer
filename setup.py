try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Business Scorer',
    'author': 'Lydia Stepanek',
    'url': '',
    'download_url': '',
    'author_email': 'lydia.stepanek@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'business-scorer'
}

setup(**config)
