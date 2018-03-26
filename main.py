# Create by :	Richard Savard
# last update :	2018-03-25
# -*- coding : utf-8 -*-
from __future__ import unicode_literals


def hash_str(s):
    """Get the int hash value of a string."""
    modulo = 0x100000001b3
    myhash = 0
    for ch in bytearray(s.encode('utf-8')):
        myhash = (31 * myhash + ch) % modulo
    return myhash


class Node(object):

    """Red-black tree node"""

    def __init__(self, khash, key):
        self.khash = khash
        self.key = key
        self.value = value
        self.red = False
        self.right = None
        self.left = None


class RedBlackTree(object):

    """Red-black tree object"""

    def __init__(self, hashing=None, compare=None):
        self._znode = Node(None, None)
        self._head = self._znode
        self._size = 0
        if hashing:
            self._hashing = hashing
        else:
            self._hashing = lambda x: x

        if compare:
            self._compare = compare
        else:
            self._compare = lambda a, b: -1 if a < b else int(a > b)

    def size(self):
        return self._size

    def put(self, key, value):
        khash = self._hashing(key)

        node = self._head
        pnode = gpnode = ggpnode = node
        while node is not self._znode:
            ggpnode = gp_node
            gpnode = p_node
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
        return "value"

    def search(self, key):
        return "value"

    def search2(self, node, key):
        return ("value", "node")

    def update(self, node, value):
        return "old value"

    # Clean memory allocation of keys and values
    def clean(callback):
        pass

    def _rotate(self, khash, key, node):
        pass

    def _split(self, khash, key, ggpnode, gpnode, pnode, node):
        pass


    

if __name__ == '__main__':
    t = RedBlackTree(hash_str)
    t.put('salut', 'valeur de salut')
    t.put('hello', 'valeur de hello')
