from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pyPodcastParser',

    version='3.1.2',

    description='pyPodcastParser is a podcast parser.',
    long_description=long_description,

    url='https://github.com/jrigden/pyPodcastParser',

    author='Jason Rigden',
    author_email='jasonrigden@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Markup :: XML',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3.14',
        'Programming Language :: Python :: 3.15',
    ],

    install_requires=[
        "beautifulsoup4",
        "lxml"
    ],

    keywords=['podcast', 'parser', 'rss', 'feed'],

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),


)
