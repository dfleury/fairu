from inspect import isclass
import unittest
import os

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
        instanceA = Fairu()
        self.assertEqual(instanceA._parent, None)
        instanceB = Fairu(parent=instanceA)
        self.assertEqual(instanceB._parent, instanceA)

    def test_existence_of_location_property(self):
        instance = Fairu()
        self.assertTrue(getattr(instance, '_start_directory', False))
        self.assertTrue(getattr(instance, '_current_directory', False))
        self.assertTrue(getattr(instance, '_previous_directory', False) is None)
        self.assertEqual(instance._start_directory, os.getcwdu())
        self.assertEqual(instance._current_directory, os.getcwdu())
        self.assertEqual(instance._previous_directory, None)

    def test_inheritance_of_history_directory_property(self):
        instanceA = Fairu()
        instanceA._current_directory = '/tmp/'
        instanceA._previous_directory = '/foo/'
        instanceB = Fairu(parent=instanceA)
        self.assertEqual(instanceA._current_directory, instanceB._current_directory)
        self.assertEqual(instanceA._previous_directory, instanceB._previous_directory)

if __name__ == '__main__':
    unittest.main()
