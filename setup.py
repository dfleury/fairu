#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from setuptools import setup

from fairu import __version__


def packages():
    packages = []
    for root, dirnames, filenames in os.walk('fairu'):
        if '__init__.py' in filenames:
            packages.append(".".join(os.path.split(root)).strip("."))

    return packages


def description():
    return open('README.md', 'r').read()


def requirements():
    lines = open('REQUIREMENTS', 'r').readlines()
    requirements = []
    for line in lines:
        requirements.append(line.replace('\n', ''))
    return requirements


def entry_points():
    ENTRY_POINTS = {}
    try:
        from setuptools import Command
    except ImportError:
        sys.stderr.write("setuptools.Command could not be imported: setuptools "
                         "extensions not available")
    else:
        ENTRY_POINTS["distutils.commands"] = [
            "test = commands.test_with_coverage:TestWithCoverage"
        ]

    return ENTRY_POINTS


if __name__ == '__main__':
    setup(name         = 'fairu',
          version      = __version__,
          description  = "Fairu is a python library to handle files easily "
                             "using a chain pattern like the jQuery framework.",
          author       = 'Diego Fleury',
          author_email = 'dfleury@gmail.com',
          license      = 'GPL',
          keywords     = "files batch process handling",
          url          = 'http://github.com/dfleury/fairu',
          packages     = packages(),
          long_description = description(),
          entry_points = entry_points(),
          classifiers  = ["Development Status :: 2 - Pre-Alpha",
                        "Intended Audience :: Developers"
                        "License :: OSI Approved :: GNU General Public "
                            "License (GPL)"
                        "Programming Language :: Python :: 2",
                        "Topic :: Software Development :: Libraries :: "
                            "Python Modules"],
          install_requires = requirements()
    )