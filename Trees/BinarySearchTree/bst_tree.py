from __future__ import annotations
from Trees import BinarySearchTreeNode


class BinarySearchTree:
    def __init__(self, root: BinarySearchTreeNode = None):
        self.root: BinarySearchTreeNode = root
        self.size: int = 0

    def add(self, data: int) -> None:
        if self.root is None:
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
        if self.root is None:
            return
        return self.__remove_helper(data, self.root)

    def __remove_helper(self, data: int, node: BinarySearchTreeNode) -> BinarySearchTreeNode:
        if node is None:
            return node
        elif data > node.data:
            node.right = self.__remove_helper(data, self.right)
        elif data < node.data:
            node.left = self.__remove_helper(data, self.left)
        else:
            if node.right is None and node.left is None:
                node = None
            elif node.right is None:
                node = node.left
                node.left = None
            elif node.left is None:
                node = node.right
                node.right = None
            else:
                tmp = self.minimum(node.right)
                node.data = tmp.data
                node.right = self.__remove_helper(tmp.data, node.right)
        return node

    def contains(self, data: int) -> bool:
        if self.root is None or data is None:
            return False
        return self.__contains_helper(data, self.root)

    def __contains_helper(self, data: int, node: BinarySearchTreeNode) -> bool:
        if data == node.data:
            return True
        if data > node.data:
            node.right = self.__contains_helper(data, node.right)
        if data < node.data:
            node.left = self.__contains_helper(data, node.left)
        return False

    def find(self, data: int) -> BinarySearchTreeNode:
        if self.root is None or data is None:
            return None
        return self.__find_helper(data, self.root)

    def __find_helper(self, data: int, node: BinarySearchTreeNode) -> BinarySearchTreeNode:
        if data == node.data:
            return node
        if data > node.data:
            node.right = self.__find_helper(data, node.right)
        if data < node.data:
            node.left = self.__find_helper(data, node.left)
        return None

    # the leftmost (smallest node) in the right subtree
    def minimum(self, node: BinarySearchTreeNode) -> BinarySearchTreeNode:
        while node.left is not None:
            return self.minimum(node.left)
        return node

    # the rightmost (largest node) in the left subtree
    def maximum(self, node: BinarySearchTreeNode) -> BinarySearchTreeNode:
        while node.right is not None:
            return self.maximum(node.right)
        return node

    """
    Find current node -> the node that has the data
    1. if right subtree is not null, successor will be the leftmost
        child of the right subtree
    2. find successor from ancestors
    """
    def successor(self, data: int) -> BinarySearchTreeNode:
        if self.root is not None:
            current: BinarySearchTreeNode = self.find(data)
            if current is None:
                return None
            if current.right is not None:
                return self.minimum(current.right)
            successor: BinarySearchTreeNode | None = None
            ancestor: BinarySearchTreeNode = self.root
            while ancestor != current:
                if current.data < ancestor.data:
                    successor = ancestor
                    ancestor = ancestor.left
                else:
                    ancestor = ancestor.right
            return successor
        return None

    """ 
        1. if right subtree is not null, successor will be the leftmost
           child of the right subtree or the right child itself
        2. If key is smaller than root node:
            a) Set the successor as root
            b) search recursively into the left subtree
    """
    def successor_alt(self, root: BinarySearchTreeNode, successor: BinarySearchTreeNode, key: int):
        if root is None:
            return None
        if key == root.data:
            if root.right is not None:
                return self.minimum(root.right)
        elif key < root.data:
            successor = root
            return self.successor_alt(root.left, successor, key)
        else:
            return self.successor_alt(root.right, successor, key)
        return successor

    """
        Find current node -> the node that has the data
        1. if left subtree is not null, predecessor will be the rightmost
            child of the left subtree
        2. find predecessor from ancestors
    """
    def predecessor(self, data: int) -> BinarySearchTreeNode:
        if self.root is not None:
            current = self.find(data)
            if current.left is not None:
                return self.maximum(current.left)
            predecessor: BinarySearchTreeNode | None = None
            ancestor: BinarySearchTreeNode = self.root
            while current != ancestor:
                if current.data > ancestor.data:
                    predecessor = ancestor
                    ancestor = ancestor.right
                else:
                    ancestor = ancestor.left
            return predecessor
        return None

    """
       1. If the left subtree is not null, the rightmost child of the
          left subtree is the predecessor or the left child itself
       2. If key is greater than the root node:
           a) set the predecessor as root
           b) search recursively to the right subtree
    """
    def predecessor_alt(self, root: BinarySearchTreeNode, predecessor: BinarySearchTreeNode, key: int) -> BinarySearchTreeNode:
        if root is None:
            return None
        if key == root.data:
            if root.left is not None:
                return self.maximum(root.left)
        if key > root.data:
            predecessor = root
            return self.predecessor_alt(root.right, predecessor, key)
        else:
            return self.predecessor_alt(root.left, predecessor, key)
        return predecessor

    # Traversals

    # preorder traversal -> root, left, right
    def preorder(self) -> None:
        return self.__preorder_helper(self.root)

    # inorder traversal -> left, root, right
    # sorts a binary search tree
    def inorder(self) -> None:
        return self.__inorder_helper(self.root)

    # postorder traversal -> left, right, root
    def postorder(self) -> None:
        return self.__postorder_helper(self.root)

    def __preorder_helper(self, node: BinarySearchTreeNode) -> None:
        if node is None:
            return
        print(node.data, end='->')
        self.__preorder_helper(node.left)
        self.__preorder_helper(node.right)

    def __inorder_helper(self, node: BinarySearchTreeNode) -> None:
        if node is None:
            return
        self.__preorder_helper(node.left)
        print(node.data, end='->')
        self.__preorder_helper(node.right)

    def __postorder_helper(self, node: BinarySearchTreeNode) -> None:
        if node is None:
            return
        self.__preorder_helper(node.left)
        self.__preorder_helper(node.right)
        print(node.data, end='->')
