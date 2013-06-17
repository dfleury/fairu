import unittest

from types import MethodType

from fairu import Fairu

class SelectTestCase(unittest.TestCase):

    def test_if_select_method_exists(self):
        assert type(Fairu().select) == MethodType

    def test_if_the_rerturn_is_the_FairuContainer(self):
        assert isinstance(Fairu().select(), Fairu)

    def test_if_FairuContainer_continues_the_chain(self):
        assert type(Fairu().select().select) == MethodType
        assert isinstance(Fairu().select().select(), Fairu)

    def test_if_fairu_returns_a_new_instance_every_use(self):
        assert Fairu().select() is not Fairu().select()

if __name__ == '__main__':
    unittest.main()
