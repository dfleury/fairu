#!/usr/bin/env python
# -*- coding: utf-8 -*-
# <Fairu - Description>
# Copyright (C) <2010-2011>  Gabriel Falcão <gabriel@nacaolivre.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import sys
import ConfigParser

from setuptools import setup

from fairu import __version__


def get_packages():
    packages = []
    for root, dirnames, filenames in os.walk('fairu'):
        if '__init__.py' in filenames:
            packages.append(".".join(os.path.split(root)).strip("."))

    return packages


def get_setup_config():
    config = ConfigParser.ConfigParser()
    config.read('setup.cfg')
    def get_setup_config():
        return config
    return config


def compile_entry_points():
    ENTRY_POINTS = {}
    try:
        from setuptools import Command
    except ImportError:
        sys.stderr.write("setuptools.Command could not be imported: setuptools "
                         "extensions not available")
    else:
        command_hook = "distutils.commands"
        ENTRY_POINTS[command_hook] = []

        # coverage
        from commands import coverage_analysis
        if coverage_analysis.COVERAGE_ANALYSIS_AVAILABLE:
            ENTRY_POINTS[command_hook].append("test = commands.coverage_ana"
                                              "lysis:CoverageAnalysis")

    return ENTRY_POINTS


if __name__ == '__main__':
    setup(name='fairu',
        version=__version__,
        description='Description',  
        author=u'Diego Fleury',
        author_email='dfleury@gmail.com',
        license='GPL',
        keywords="files batch proccess handling",
        url='http://github.com/dfleury/fairu',
        packages=get_packages(),
        long_description=open('README.md').read(),
        entry_points=compile_entry_points(),
        classifiers=["Development Status :: 1 - Planning",
                     "Programming Language :: Python :: 2",
                     "Topic :: Software Development :: Libraries :: "
                         "Python Modules"],
    )