from __future__ import  annotations
# from typing import TypeVar, Generic, Type, Union
# NodeType = Type[Node]


class Node:
    def __init__(self, data: int = 0, next_node: Node = None) -> None:
        self.data = data
        self.next = next_node

    def get_data(self) -> int:
        return self.data

    def set_data(self, data: int) -> None:
        self.data = data

    def get_next(self) -> Node:
        return self.next

    def set_next(self, node: Node) -> None:
        self.next = node


class SinglyLinkedList:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None
        self.size: int = 0

    def add_first(self, data: int) -> None:
        node = Node(data)
        if self.head is None:
            self.head = self.tail = Node(data)
        else:
            node.next = self.head
            self.head = node
        self.size += 1

    def add_last(self, data: int) -> None:
        node = Node(data)
        if self.head is None:
            self.add_first(data)
        self.tail.next = node
        self.tail = node

    def remove_first(self) -> None:
        if self.head is not None:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
            self.size -= 1
            return
        return

    def remove_last(self) -> None:
        if self.head is not None:
            if self.head == self.tail:
                self.remove_first()
            else:
                current = self.head
                prev = None
                while current.next is not None:
                    prev = current
                    current = current.next
                prev.next = None
                self.tail = prev
                self.size -= 1
            return
        return

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
