from __future__ import annotations
from Trees import AVLTreeNode


class AVLTree:
    def __init__(self, root: AVLTree = None):
        self.root = root
        self.size = 0

    def insert(self, data: int) -> None:
        if self.root is None:
            self.root = AVLTreeNode(data)
            return
        self.__insert_helper(data, self.root)
        self.__update_balance(self.root)

    def __insert_helper(self, data: int, node: AVLTreeNode) -> None:
        new_node = AVLTreeNode(data)
        if data == node.data:
            return
        if data > node.data:
            if node.right is None:
                node.right = new_node
                new_node.parent = node
                self.size += 1
                return
            self.__insert_helper(data, node.right)
            return
        if node.left is None:
            node.left = new_node
            new_node.parent = node
            self.size += 1
            return
        self.__insert_helper(data, node.left)
        return

    def remove(self, data: int) -> AVLTreeNode:
        pass

    def __remove_helper(self, data: int, node: AVLTreeNode) -> AVLTreeNode:
        pass

    def __update_balance(self, node: AVLTreeNode) -> None:
        pass

    def __rebalance(self, node: AVLTreeNode) -> None:
        pass

    def right_rotate(self, node: AVLTreeNode) -> None:
        pass

    def left_rotate(self, node: AVLTreeNode) -> None:
        pass

    def left_right_rotate(self, node: AVLTreeNode) -> None:
        pass

    def right_left_rotate(self, node: AVLTreeNode) -> None:
        pass