from __future__ import annotations


class AVLTreeNode:
    def __init__(self, data: int, left: AVLTreeNode = None, right: AVLTreeNode = None, parent: AVLTreeNode = None) -> None:
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

    def get_data(self) -> int:
        return self.data

    def set_data(self, data: int) -> None:
        self.data = data

    def get_right(self, right: AVLTreeNode) -> None:
        self.right = right

    def set_right(self, right: AVLTreeNode) -> None:
        self.right = right

    def get_left(self, left: AVLTreeNode) -> None:
        self.left = left

    def set_left(self, left: AVLTreeNode) -> None:
        self.left = left

    def get_parent(self, parent: AVLTreeNode) -> None:
        self.parent = parent

    def set_parent(self, parent: AVLTreeNode) -> None:
        self.parent = parent
