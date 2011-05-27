import unittest

import fairu

class  CoreTestCase(unittest.TestCase):

    def test_if_the_meta_informations_are_ok(self):
        assert fairu.__author__ == "Diego Fleury"
        assert fairu.__version__ == "0.1"

if __name__ == '__main__':
    unittest.main()
