import collections
import os

import filtering


START_DIRECTORY = os.getcwdu()


class Fairu(object):

    def __init__(self, parent=None):
        self._elements = []
        self._iterator_index = 0
        self._parent = parent
        self._start_directory = START_DIRECTORY
        self._current_directory = self._start_directory
        self._previous_directory = None

        if isinstance(self._parent, Fairu):
            self._current_directory = self._parent._current_directory
            self._previous_directory = self._parent._previous_directory

    def __iter__(self):
        self._iterator_index = 0
        return self

    def __len__(self):
        return len(self._elements)

    def next(self):
        if self._iterator_index == len(self._elements):
            raise StopIteration
        else:
            element = self._elements[self._iterator_index]
            self._iterator_index += 1
            return element

    def add(self, items):
        if type(items) == file:
            self._elements.append(items)
        elif isinstance(items, collections.Iterable):
            for item in items:
                self.add(item)
        return self

    def select(self, filter):
        return filtering.select(self, filter)
