#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from setuptools import setup


def packages():
    packages = []
    for root, dirnames, filenames in os.walk('fairu'):
        if '__init__.py' in filenames:
            packages.append(".".join(os.path.split(root)).strip("."))

    return packages


def description():
    return open('README.md', 'r').read()


if __name__ == '__main__':
    setup(
        name='fairu',
        version='0.1',
        description="Fairu is a python library to handle files easily using a chain pattern like the jQuery framework.",
        author='Diego Fleury',
        author_email='dfleury@gmail.com',
        license='GPL',
        keywords="files batch process handling",
        url='http://github.com/dfleury/fairu',
        packages=packages(),
        long_description=description(),
        classifiers=[
            "Development Status :: 2 - Pre-Alpha",
            "Intended Audience :: Developers"
            "License :: OSI Approved :: GNU General Public License (GPL)"
            "Programming Language :: Python :: 2",
            "Topic :: Software Development :: Libraries :: Python Modules"
        ],
        test_suite='tests',
    )
