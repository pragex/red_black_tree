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

    def __init__(self, key, key_hash):
        self.key_hash = key_hash
        self.key = key
        self.value = value
        self.red = False
        self.right = None
        self.left = None


class RedBlackTree(object):

    """Red-black tree"""

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
        key_hash = self._hashing(key)

        node = self._head
        p_node = g_node = gg_node = node
        while node is not self._znode:
            gg_node = g_node
            g_node = p_node
            p_node = node

            if key_hash < node.key_hash or (key_hash == node.key_hash and
                                            self._compare(key, node.key) < 0):
                node = node.left
            else:
                node = node.right

            if node.left.red and node.right.red:
                self._split(key, key_hash)

        mynode = Node(key_hash, key, value)
        mynode.value = value
        mynode.left = self._znode
        mynode.right = self._znode
        self._split(key, key_hash)

        self._size += 1
        return True

    def _rotate(self, key, key_hash, head):
        if key_hash is None:
            key_hash = self._hashing(key)

    def _split(self, key, key_hash):
        if key_hash is None:
            key_hash = self._hashing(key)

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

if __name__ == '__main__':
    t = RedBlackTree(hash_str)
    t.put('salut', 'valeur de salut')
    t.put('hello', 'valeur de hello')
