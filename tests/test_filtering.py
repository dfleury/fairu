import unittest
from types import MethodType

from fairu import Fairu


class SelectTestCase(unittest.TestCase):

    def test_if_select_method_exists(self):
        self.assertEqual(type(Fairu().select), MethodType)

    def test_if_select_continues_the_chain(self):
        self.assertTrue(isinstance(Fairu().select(None), Fairu))
        self.assertEqual(type(Fairu().select(None).select), MethodType)
        self.assertTrue(isinstance(Fairu().select(None).select(None), Fairu))

    def test_select_returns_a_new_instance_every_use(self):
        self.assertIsNot(Fairu().select(None), Fairu().select(None))
        instanceA = Fairu().select(None)
        instanceB = instanceA.select(None)
        self.assertIsNot(instanceA, instanceB)
        self.assertIs(instanceB._parent, instanceA)

if __name__ == '__main__':
    unittest.main()
