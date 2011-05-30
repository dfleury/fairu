#! /usr/bin/env python

"""
Fairu testing suite.
"""

import unittest
import re
import os
import sys

def get_test_suite(test_file_names=None):
    """
    Build a testsuite with given tests
    """
    if test_file_names is None:
        test_file_names = get_test_file_names()
    tests = unittest.defaultTestLoader.loadTestsFromNames(test_file_names)
    return unittest.TestSuite(tests)

def get_test_file_names():
    """
    Get list of test file names.
    """
    path = os.path.dirname(__file__)
    files = os.listdir(path)
    ignore = ('__init__.py', 'coverage')
    ignore_pyc = re.compile(r"\.py$", re.IGNORECASE)
    test_files = []
    for f in files:
        if not f in ignore and ignore_pyc.search(f):
            relative_path = os.path.relpath(path)
            if relative_path == '.':
                test_files.append(os.path.splitext(f)[0])
            else:
                test_files.append("%s.%s" %
                                  (relative_path, os.path.splitext(f)[0]))
    return test_files

def run(test_module=None):
    """
    Runs the testsuite
    """
    
    if test_module and isinstance(test_module, str):
        test_module = [test_module.replace('.py', '').replace('/', '.')]

    runner = unittest.TextTestRunner()
    runner.run(get_test_suite(test_module))

if __name__ == "__main__":
    test_module = None
    if len(sys.argv) == 2:
        test_module = sys.argv[1]
    run(test_module)