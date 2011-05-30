"""
Runs the tests
"""
import subprocess
from sys import stderr

from setuptools import Command


class TestWithCoverage(Command):
    """
    Code coverage analysis command.
    """
    description = "run test with coverage analysis"
    user_options = [
        ('test-module=', 't', "explicitly specify a module to "
                                  "test (e.g. 'fairu.selector')"),
    ]

    def initialize_options(self):
        self.test_module = None

    def finalize_options(self):
        pass

    def run(self):
        self.analyse()
        self.report()

    def analyse(self):
        self.make_call('run')

    def report(self):
        self.make_call('report')

    def make_call(self, command):
        try:
            callOptions = self.get_options(command)
            retcode = subprocess.call(callOptions)
            if retcode < 0:
                stderr.write("Process was terminated during the %s by signal" %
                                 "running" if command == 'run' else 'reporting')
            elif retcode > 0:
                stderr.write("Some problems did occur...")
        except OSError, e:
            stderr.write("Execution failed:", e)

    def get_options(self, command):
        callOptions = ['coverage', command]

        if command == 'run':
            callOptions.append('tests/__init__.py')
            if self.test_module and isinstance(self.test_module, str):
                callOptions.append(self.test_module)
                
        elif command == 'report':
            callOptions.append('-m')

        return callOptions