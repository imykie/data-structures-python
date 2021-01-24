from __future__ import annotations
from Trees import RBTreeNode

"""
Red Black Trees Conditions:
1. It is a self-balancing Binary Search Tree
2. All nodes are either Red or Black
3. All leaf nodes are Black
4. A parent that is a red node cannot have a red child
5. The Number of Black node must be the same for all path

Insertion:
1. If tree is empty, create new node as root with color Black
2. If tree is not empty, create new node as leaf with color Red
3. If parent of new node is Black then exit.
4. If parent of new node is Red, the check the color of the parent's sibling (the aunt node)
    a. if color is Black or null then do suitable rotation and recolor
    b. if color is Red then recolor and also check if parent's parent is not root node then recolor it and recheck
    

"""


class RBTree:
    def __init__(self, root: RBTreeNode = None):
        self.root = root
        self.size = 0

