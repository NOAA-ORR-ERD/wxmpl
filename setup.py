#!/usr/bin/env python

# Name: setup.py
# Purpose: wxmpl distutils install program
# Author: Ken McIvor <mcivor@iit.edu>
#         Carlo Segre <segre@iit.edu>
#         Chris Barker <Chris.Barker@noaa.gov>
#
# Copyright 2005-2011 Illinois Institute of Technology
#
# See the file "LICENSE" for information on usage and redistribution
# of this file, and for a DISCLAIMER OF ALL WARRANTIES.


from __future__ import (absolute_import, division, print_function)

import os
import sys
from setuptools import find_packages, setup
from setuptools.command.test import test as TestCommand

rootpath = os.path.split(__file__)[0]

long_description = open(os.path.join(rootpath, 'README.rst')).read()


def extract_version(module='wxmpl.py'):
    version = None
    fname = os.path.join(rootpath, module)
    with open(fname) as f:
        for line in f:
            if (line.startswith('__version__')):
                _, version = line.split('=')
                version = version.strip()[1:-1]  # Remove quotation characters.
                break
    return version


setup(
    name='wxmpl',
    version=extract_version(),
    author='Ken McIvor, Carlo Segre, Chris Barker',
    author_email='Chris.Barker@noaa.gov, segre@iit.edu',
    description=('A library for painlessly embedding matplotlib in wxPython'),
    license='MIT',
    url='https://github.com/NOAA-ORR-ERD/wxmpl',
    long_description=long_description,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Utilities',
        'Topic :: Desktop Environment :: wxPython'
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        ],
    py_modules=['wxmpl'],
    scripts=['plotit'],
    )

