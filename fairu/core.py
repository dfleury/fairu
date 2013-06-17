import filtering


class Fairu(object):

    def __init__(self):
        self._elements = []
        self._iterator_index = 0
        self._parent = None

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

    def select(self, filter):
        return filtering.select(self, filter)
