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
    def __init__(self, key, key_hash, value):
        self.key_hash = key_hash
        self.key = key
        self.value = value
        self.colored = False
        self.right = None
        self.left = None


class RedBlackTree(object):
    """Red-black tree"""
    def __init__(self, hashing=None, compare=None):
        self._null = Node(None, None, None)
        self._root = None
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
        pass

    def pop(self, key):
        return "value"

    def search(self, key):
        return "value"

    def search2(self, node, key):
        return ("value", "node")

    def update(self, node, value):
        return "old value"


if __name__ == '__main__':
    t = RedBlackTree(hash_str)
