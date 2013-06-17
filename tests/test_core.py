import unittest
from inspect import isclass

from fairu import Fairu


class CoreTestCase(unittest.TestCase):

    elements = ['w', 'o', 'r', 'k', 's']

    def test_if_Fairu_class_is_avaliable_importing_fairu_module(self):
        import fairu
        self.assertTrue(getattr(fairu, 'Fairu', False))
        self.assertTrue(isclass(fairu.Fairu))

    def test_if_is_iterable(self):
        self.assertTrue(getattr(Fairu(), '__iter__', False))
        self.assertTrue(getattr(Fairu(), 'next', False))
        self.assertTrue(getattr(Fairu(), '__len__', False))

    def test_if_Fairu_instance_can_be_iterabled_by_for_in(self):
        instance = Fairu()
        instance._elements = self.elements
        elements = []
        for element in instance:
            elements.append(element)
        self.assertEqual(self.elements, elements)

    def test_if_the_iterator_rewinds_for_a_second_iteration(self):
        instance = Fairu()
        instance._elements = self.elements
        count_iterations = [0, 0]
        for element in instance:
            count_iterations[0] += 1
        for element in instance:
            count_iterations[1] += 1
        self.assertEqual(count_iterations[0], count_iterations[1])

    def test_if_len_function_works_with_Fairu_instance(self):
        instance = Fairu()
        self.assertEqual(len(instance), 0)
        instance._elements = self.elements
        self.assertEqual(len(instance), len(self.elements))

    def test_if_Fairu_have_a_parent_set_of_elements(self):
        self.assertEqual(Fairu()._parent, None)

if __name__ == '__main__':
    unittest.main()
