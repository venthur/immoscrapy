#!/usr/bin/env python


from setuptools import setup

meta = {}
exec(open('./immoscrapy/version.py').read(), meta)
meta['long_description'] = open('./README.md').read()

setup(
    name='immoscrapy',
    version=meta['__VERSION__'],
    description='Scrape Immobilienscout24 data using Python.',
    long_description=meta['long_description'],
    long_description_content_type='text/markdown',
    keywords='immobilienscout24 immoscout cli python scraper',
    author='Bastian Venthur',
    author_email='mail@venthur.de',
    url='https://github.com/venthur/immoscrapy',
    project_urls={
        'Documentation': 'https://immoscrapy.readthedocs.io/',
        'Source': 'https://github.com/venthur/immoscrapy',
        'Changelog':
            'https://github.com/venthur/immoscrapy/blob/master/CHANGELOG.md',
    },
    python_requires='>=3.7',
    install_requires=[
        'requests',
    ],
    packages=['immoscrapy'],
    entry_points={
        'console_scripts': [
            'immoscrapy = immoscrapy.cli:main'
        ]
    },
    license='MIT',
)
