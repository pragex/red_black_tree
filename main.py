# -*- coding : utf-8 -*-
# Create by: Richard Savard

from __future__ import unicode_literals
from abc import ABC


class BaseNode(ABC):
    """Red-black tree base node"""



class Node(BaseNode):
    """Red-black tree string node"""
    
    def __init__(self, key, value=None):
        self.khash = khash
        self.key = key
        self.value = value
        self.red = False
        self.right = None
        self.left = None


    def compareTo(self, key):
        return -1

        
    @methodestatic
    def hashing(key):
        """Get the int hash value of a string"""
        modulo = 0xFFFFFFFB
        myhash = 0
        for i, ch in enumarate(bytearray(key.encode('utf-8'))):
            myhash = (31 * myhash + ch) % modulo
            if i >= 1000:
                break
        return myhash


class RedBlackTree(object):

    """Red-black tree object"""

    def __init__(self):
        self._znode = Node()
        self._head = self._znode
        self._count = 0
        if hashing:
            self._hashing = hashing
        else:
            self._hashing = lambda x: x

        if compare:
            self._compare = compare
        else:
            self._compare = lambda a, b: -1 if a < b else int(a > b)

    def count(self):
        return self._count

    def put(self, key, value):
        khash = self._hashing(key)

        node = self._head
        pnode = gpnode = ggpnode = node
        while node is not self._znode:
            ggpnode = gpnode
            gpnode = pnode
            pnode = node

            if khash < node.khash or (khash == node.khash and
                                      self._compare(key, node.key) < 0):
                node = node.left
            else:
                node = node.right

            if node.left.red and node.right.red:
                self._split(khash, key, ggpnode, gpnode, pnode, node)

        mynode = Node(khash, key)
        mynode.value = value
        mynode.left = self._znode
        mynode.right = self._znode
        self._split(khash, key, ggpnode, gpnode, pnode, mynode)

        self._size += 1
        return True

    def pop(self, key):
        return "old value"

    def search(self, key):
        return "value"

    def update(self, node, value):
        return "old value"

    def _rotate(self, khash, key, node):
        pass

    def _split(self, khash, key, ggpnode, gpnode, pnode, node):
        pass


if __name__ == '__main__':
    t = RedBlackTree()
    t.put('salut', 'valeur de salut')
    t.put('hello', 'valeur de hello')
