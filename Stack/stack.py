from __future__ import annotations
from LinkedList import SinglyLinkedList


class Stack:
    def __init__(self):
        self.linked_list = SinglyLinkedList()

    def is_empty(self) -> bool:
        return True if self.linked_list.size > 0 else False

    def push(self, data) -> None:
        self.linked_list.add_last(data)

    def pop(self) -> None:
        self.linked_list.remove_last()

    def peek(self) -> int:
        return self.linked_list.tail.data
