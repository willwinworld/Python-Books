#! python3
# -*- coding: utf-8 -*-
from collections.abc import Sequence

class FrequencyList(list):
    def __init__(self, members):
        super().__init__(members)

    def frequency(self):
        counts = {}
        for item in self:
            counts.setdefault(item, 0)
            counts[item] += 1
        return counts


# foo = FrequencyList(['a', 'b', 'a', 'c', 'b', 'a', 'd'])
# print('Length is', len(foo))
# foo.pop()
# print('After pop:', repr(foo))
# print('Frequency:', foo.frequency())


class BinaryNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class IndexableNode(BinaryNode):
    def _search(self, count, index):
        # Returns(found, count)

    def __getitem__(self, index):
        found, _ = self._search(0, index)
        if not found:
            raise IndexError('Index out of range')
        return found.value


tree = IndexableNode(
    10,
    left=IndexableNode(
        5,
        left=IndexableNode(2),
        right=IndexableNode(
            6, right=IndexableNode(7))),
    right=IndexableNode(
        15, left=IndexableNode(11)))


print('LRR=', tree.left.right.right.value)
print('Index 0 =', tree[0])
print('Index 1 =', tree[1])
print('11 in the tree?', 11 in tree)
print('17 in the tree?', 17 in tree)
print('Tree is', list(tree))


class SequenceNode(IndexableNode):
    def __len__(self):
        _, count = self._search(0, None)
        return count
