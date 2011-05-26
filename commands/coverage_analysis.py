"""
Support for coverage analysis.
"""
import os

import unittest
import shutil
import logging

from tests import get_test_suite


COVERAGE_ANALYSIS_AVAILABLE = False
try:
    from setuptools import Command
except ImportError:
    logging.warn(
        "setuptools.Command could not be imported: setuptools extensions "
        "not available")
else:
    try:
        import coverage
    except ImportError:
        logging.warn(
            "coverage could not be imported: test coverage "
            "analysis not available")
    else:
        logging.info(
            "coverage imported successfully: test coverage "
            "analysis available")
        COVERAGE_ANALYSIS_AVAILABLE = True


class CoverageAnalysis(Command):
    """
    Code coverage analysis command.
    """

    description = "run test coverage analysis"
    user_options = [
            ('erase', None, "remove all existing coverage results"),
            ('branch', 'b', "measure branch coverage in addition to "
                            "statement coverage"),
            ('test-module=', 't', "explicitly specify a module to "
                                  "test (e.g. 'fairu.selector')"),
            ('no-annotate', None, "do not create annotated source code files"),
            ('no-html', None, "do not create HTML report files"),]

    def initialize_options(self):
        """
        Initialize options to default values.
        """
        self.branch = False
        self.coverage_dir = None
        self.erase = False
        self.no_annotate = False
        self.no_html = False
        self.report_dir = None
        self.report_source_dir = None
        self.test_module = None

    def finalize_options(self):
        pass

    def run(self):
        """
        Main command implementation.
        """

        if self.erase:
            logging.warn(
                "removing coverage results directory: '%s'" %
                    self.coverage_dir)
            try:
                shutil.rmtree(self.coverage_dir)
            except Exception:
                pass
        else:
            logging.info("running coverage analysis...")

            if self.test_module is None:
                test_suite = get_test_suite()
            else:
                test_suite = get_test_suite([self.test_module])
            
            runner = unittest.TextTestRunner()
            cov = coverage.coverage(branch=self.branch)

            cov.start()
            runner.run(test_suite)
            cov.stop()

            print("\r\n\r\n\r\nCOVERAGE REPORT:")

            if not self.no_annotate:
                cov.annotate(directory=self.report_source_dir)

            if not self.no_html:
                cov.html_report(directory=self.report_dir)

            cov.report()
            print("")