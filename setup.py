try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {

    'description': 'Skeleton Project - changme',
    'author': 'Morizel Hodges Jr',
    'url': 'URL to get it',
    'download_url': 'where to download it',
    'author_email': 'mhodgesjr2010@gmail.com',
    'version': '1.0',
    'install_requires':['nose'],
    'packages':['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
