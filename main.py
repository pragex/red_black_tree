# -*- coding : utf-8 -*-
# Create by: Richard Savard

from __future__ import unicode_literals


class NodeItem(object):

    """Red-black tree node"""

    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.red = False
        self.right = None
        self.left = None
        print("NodeItem({1}) => {0}".format(self._key, self._hash))

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, key):
        """Set the key value"""
        self._hash = self.hashing(key)
        self._key = key

    @staticmethod
    def hashing(key):
        return hash(key)


class RedBlackTree(object):

    """Red-black tree object"""

    def __init__(self, node_type):
        self._node_item = node_type
        self._znode = None
        self._head = self._znode
        self._count = 0

    def count(self):
        return self._count

    def put(self, key, value):
        mynode = self._node_item(key)
        
        """
        node = self._head
        pnode = gpnode = ggpnode = node
        while node is not self._znode:
            ggpnode = gpnode
            gpnode = pnode
            pnode = node

            if node.key < key:
                node = node.left
            else:
                node = node.right

            if node.left.red and node.right.red:
                self._split()

        mynode = self._node_item(key)
        mynode.value = value
        mynode.left = self._znode
        mynode.right = self._znode
        self._split()

        self._size += 1
        """
        return True

    def pop(self, key):
        return "old value"

    def search(self, key):
        return "value"

    def update(self, key, value):
        return "old value"

    def _rotate(self):
        pass

    def _split(self):
        pass


if __name__ == '__main__':
    t = RedBlackTree(NodeItem)
    t.put('salut', 'valeur de salut')
    t.put('hello', 'valeur de hello')


# @staticmethod
# def hashing(key):
#    """Get the int hash value of a string"""
#    modulo = 0xFFFFFFFB
#    myhash = 0
#    for i, ch in enumerate(bytearray(key.encode('utf-8'))):
#        myhash = (31 * myhash + ch) % modulo
#        if i >= 1000:
#            break
#    return myhash
