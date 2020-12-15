from __future__ import annotations
from Trees import BinarySearchTreeNode
from collections import deque


class BinarySearchTree:
    def __init__(self, root: BinarySearchTreeNode = None):
        self.root: BinarySearchTreeNode = root
        self.size: int = 0

    def insert(self, data: int) -> None:
        if self.root is None:
            self.root = BinarySearchTreeNode(data)
        else:
            self.__insert_helper(data, self.root)

    def __insert_helper(self, data: int, node: BinarySearchTreeNode) -> None:
        if data == node.data:
            return
        if data > node.data:
            if node.right is None:
                node.right = BinarySearchTreeNode(data)
                self.size += 1
                return
            self.__insert_helper(data, node.right)
            return

        if node.left is None:
            node.left = BinarySearchTreeNode(data)
            self.size += 1
            return
        self.__insert_helper(data, node.left)
        return

    def delete(self, data: int) -> BinarySearchTreeNode:
        return self.__delete_helper(data, self.root)

    def __delete_helper(self, data: int, node: BinarySearchTreeNode) -> BinarySearchTreeNode:
        if node is None:
            return node
        if data > node.data:
            node.right = self.__delete_helper(data, node.right)
        elif data < node.data:
            node.left = self.__delete_helper(data, node.left)
        else:
            if node.right is None and node.left is None:
                node = None
            elif node.right is None:
                node = node.left
            elif node.left is None:
                node = node.right
            else:
                tmp = self.minimum(node.right)
                node.data = tmp.data
                node.right = self.__delete_helper(tmp.data, node.right)
            self.size -= 1
        return node

    def contains(self, data: int) -> bool:
        return self.__contains_helper(data, self.root)

    def __contains_helper(self, data: int, node: BinarySearchTreeNode) -> bool:
        if node is None:
            return False
        if data == node.data:
            return True
        if data > node.data:
            return self.__contains_helper(data, node.right)
        return self.__contains_helper(data, node.left)

    def find(self, data: int) -> BinarySearchTreeNode:
        return self.__find_helper(data, self.root)

    def __find_helper(self, data: int, node: BinarySearchTreeNode) -> BinarySearchTreeNode:
        if node is None:
            return None
        if data == node.data:
            return node
        if data > node.data:
            return self.__find_helper(data, node.right)
        return self.__find_helper(data, node.left)

    # the leftmost (smallest node) in the right subtree
    def minimum(self, node: BinarySearchTreeNode) -> BinarySearchTreeNode:
        while node.left is not None:
            node = node.left
        return node

    # the rightmost (largest node) in the left subtree
    def maximum(self, node: BinarySearchTreeNode) -> BinarySearchTreeNode:
        while node.right is not None:
            node = node.right
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
        elif key > root.data:
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
        if node:
            print(str(node.data)+' -> ', end='')
            self.__preorder_helper(node.left)
            self.__preorder_helper(node.right)

    def __inorder_helper(self, node: BinarySearchTreeNode) -> None:
        if node:
            self.__inorder_helper(node.left)
            print(str(node.data) + ' -> ', end='')
            self.__inorder_helper(node.right)

    def __postorder_helper(self, node: BinarySearchTreeNode) -> None:
        if node:
            self.__postorder_helper(node.left)
            self.__postorder_helper(node.right)
            print(str(node.data) + ' -> ', end='')

    def invert(self) -> BinarySearchTreeNode:
        return self.__invert_helper(self.root)

    def __invert_helper(self, node: BinarySearchTreeNode) -> BinarySearchTreeNode:
        if node is not None:
            temp = node.left
            node.left = node.right
            node.right = temp
            self.__invert_helper(node.left)
            self.__invert_helper(node.right)
        return node

    def get_size(self) -> int:
        return self.size

    def print_tree(self) -> None:
        self.__print_tree_helper(self.root)

    def __print_tree_helper(self, root: BinarySearchTreeNode) -> None:
        res = []
        q = deque([root])
        while q:
            row = []
            for _ in range(len(q)):
                node = q.popleft()
                if not node:
                    row.append("#")
                    continue
                row.append(node.data)
                q.append(node.left)
                q.append(node.right)
            res.append(row)
        rows = len(res)
        base = 2 ** (rows)
        for r in range(rows):
            for v in res[r]:
                print("." * (base), end="")
                print(v, end="")
                print("." * (base - 1), end="")
            print("|")
            base //= 2
