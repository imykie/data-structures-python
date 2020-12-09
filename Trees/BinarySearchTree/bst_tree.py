from __future__ import annotations
from Trees import BinarySearchTreeNode


class BinarySearchTree:
    def __init__(self, root: BinarySearchTreeNode = None):
        self.root: BinarySearchTreeNode = root
        self.size: int = 0

    def add(self, data: int) -> None:
        if self.root.data is None:
            self.root = BinarySearchTreeNode(data)
        else:
            self.__add_helper(data, self.root)
        self.size += 1

    def __add_helper(self, data: int, node: BinarySearchTreeNode) -> None:
        if node.data == data:
            return
        if node.data > data:
            if node.right is None:
                node.right = BinarySearchTreeNode(data)
                return
            self.__add_helper(data, node.right)
            return

        if node.left is None:
            node.left = BinarySearchTreeNode(data)
            return
        self.__add_helper(data, node.left)
        return

    def remove(self, data: int) -> BinarySearchTreeNode:
        pass

    def __remove_helper(self, data: int, node: BinarySearchTreeNode) -> BinarySearchTreeNode:
        pass

    def contains(self, data: int) -> bool:
        pass

    def __contains_helper(self, data: int) -> bool:
        pass

    def minimum(self, node: BinarySearchTreeNode) -> BinarySearchTreeNode:
        pass

    def maximum(self, node: BinarySearchTreeNode) -> BinarySearchTreeNode:
        pass

    def successor(self, root: BinarySearchTreeNode, successor: BinarySearchTreeNode, key: int) -> BinarySearchTreeNode:
        pass

    def predecessor(self, root: BinarySearchTreeNode, successor: BinarySearchTreeNode, key: int) -> BinarySearchTreeNode:
        pass

    # Traversals

    # preorder traversal -> root, left, right
    def preorder(self):
        pass

    # inorder traversal -> left, root, right
    # sorts a binary search tree
    def inorder(self):
        pass

    # postorder traversal -> left, right, root
    def postorder(self):
        pass

    def __preorder_helper(self, node: BinarySearchTreeNode) -> None:
        pass

    def __inorder_helper(self, node: BinarySearchTreeNode) -> None:
        pass

    def __postorder_helper(self, node: BinarySearchTreeNode) -> None:
        pass

