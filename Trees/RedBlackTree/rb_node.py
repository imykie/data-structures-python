from __future__ import annotations


class RBTreeNode:
    def __init__(self,
                 data: int = 0,
                 left: RBTreeNode = None,
                 right: RBTreeNode = None,
                 parent: RBTreeNode = None,
                 black: bool = False,
                 is_left_child: bool = False
                 ) -> None:
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent
        self.black = black
        self.is_left_child = is_left_child

    def get_data(self) -> int:
        return self.data

    def set_data(self, data: int) -> None:
        self.data = data

    def get_right(self, right: RBTreeNode) -> None:
        self.right = right

    def set_right(self, right: RBTreeNode) -> None:
        self.right = right

    def get_left(self, left: RBTreeNode) -> None:
        self.left = left

    def set_left(self, left: RBTreeNode) -> None:
        self.left = left

    def get_parent(self, parent: RBTreeNode) -> None:
        self.parent = parent

    def set_parent(self, parent: RBTreeNode) -> None:
        self.parent = parent
