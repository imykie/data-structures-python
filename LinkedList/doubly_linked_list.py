from __future__ import annotations


class Node:
    def __init__(self, data: int = 0, next_node: Node = None, prev_node: Node = None) -> None:
        self.data = data
        self.next = next_node
        self.prev = prev_node

    def get_data(self) -> int:
        return self.data

    def set_data(self, data: int) -> None:
        self.data = data

    def get_next(self) -> Node:
        return self.next

    def set_next(self, node: Node) -> None:
        self.next = node

    def get_prev(self) -> Node:
        return self.prev

    def set_prev(self, node: Node) -> None:
        self.prev = node

