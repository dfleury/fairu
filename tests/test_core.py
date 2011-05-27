import unittest

from inspect import isclass

import fairu

class  CoreTestCase(unittest.TestCase):

    def test_if_have_a_version(self):
        assert fairu.__version__ == "0.1"

    def test_if_Fairu_class_is_avaliable_importing_fairu_module(self):
        assert getattr(fairu, 'Fairu', False) != False
        assert isclass(fairu.Fairu)

if __name__ == '__main__':
    unittest.main()
