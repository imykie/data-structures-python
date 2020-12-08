from __future__ import annotations


class BinarySearchTreeNode:
    def __init__(self, data: int = 0, right: BinarySearchTreeNode = None, left: BinarySearchTreeNode = None) -> None:
        self.data: int = data
        self.right: BinarySearchTreeNode = right
        self.left: BinarySearchTreeNode = left

    def get_data(self) -> int:
        return self.data

    def set_data(self, data: int) -> None:
        self.data = data

    def get_right(self, right: BinarySearchTreeNode) -> None:
        self.right = right

    def set_right(self, right: BinarySearchTreeNode) -> None:
        self.right = right

    def get_left(self, left: BinarySearchTreeNode) -> None:
        self.left = left

    def set_left(self, left: BinarySearchTreeNode) -> None:
        self.left = left

