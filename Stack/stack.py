from __future__ import annotations
from LinkedList import SinglyLinkedList


class Stack:
    def __init__(self):
        self.linked_list = SinglyLinkedList()

    def is_empty(self) -> bool:
        return False if self.linked_list.size > 0 else True

    def push(self, data: int) -> None:
        self.linked_list.add_last(data)

    def pop(self) -> None:
        self.linked_list.remove_last()

    def peek(self) -> int:
        return self.linked_list.tail.data if self.linked_list.head is not None else None


class StackArr:
    def __init__(self):
        self.data = []

    def is_empty(self) -> bool:
        return False if len(self.data) > 0 else True

    def push(self, data: int) -> None:
        self.data.append(data)

    def pop(self) -> None:
        self.data.pop()

    def peek(self) -> int:
        return self.data[len(self.data) - 1] if len(self.data) > 0 else None
