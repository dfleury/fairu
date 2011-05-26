import unittest

import fairu

class  TestCoreTestCase(unittest.TestCase):

    def test_if_the_meta_informations_are_ok(self):
        self.assertEqual(fairu.__author__, "Diego Fleury")
        self.assertEqual(fairu.__version__, "0.1")

if __name__ == '__main__':
    unittest.main()
