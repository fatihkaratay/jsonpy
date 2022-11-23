#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='jsonpy',
    version='1.0',
    packages=['jsonpy'],

    url='https://github.com/fatihkaratay/jsonpy',
    author='Fatih Karatay',
    author_email='fatihkaratay@gmail.com',
    description='Jsonpy is a schema for Python',
    license='MIT',

    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Development Status :: 1 - Planning',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
