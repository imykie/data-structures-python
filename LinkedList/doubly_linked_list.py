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


class DoublyLinkedList:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None
        self.size: int = 0

    def add_first(self, data: int) -> None:
        pass

    def add_last(self, data: int) -> None:
        pass

    def remove_first(self) -> None:
        pass

    def remove_last(self) -> None:
        pass

    def remove(self, data: int) -> None:
        pass

    def remove_at_position(self, pos: int) -> None:
        pass

    def contains(self, data: int) -> bool:
        pass

    def insert(self, data: int, pos: int) -> None:
        pass

    def replace(self, data: int, pos) -> None:
        pass

    def find(self, data: int) -> int:
        pass

    def display(self) -> None:
        pass

    def reverse(self) -> None:
        pass

    def no_of_occurrence(self, data: int) -> None:
        pass
