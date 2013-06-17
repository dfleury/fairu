import unittest
from types import MethodType

from fairu import Fairu


class SelectTestCase(unittest.TestCase):

    def test_if_select_method_exists(self):
        assert type(Fairu().select) == MethodType

    def test_if_the_rerturn_is_the_Fairu(self):
        assert isinstance(Fairu().select(None), Fairu)

    def test_if_Fairu_continues_the_chain(self):
        assert type(Fairu().select(None).select) == MethodType
        assert isinstance(Fairu().select(None).select(None), Fairu)

    def test_if_fairu_returns_a_new_instance_every_use(self):
        assert Fairu().select(None) is not Fairu().select(None)
        instanceA = Fairu().select(None)
        instanceB = instanceA.select(None)
        assert instanceA is not instanceB
        assert instanceB._parent is instanceA

if __name__ == '__main__':
    unittest.main()
