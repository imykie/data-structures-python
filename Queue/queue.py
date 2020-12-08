from __future__ import annotations
from LinkedList import SinglyLinkedList


class Queue:
    def __init__(self):
        self.linked_list = SinglyLinkedList()

    def is_empty(self):
        return False if self.linked_list.size > 0 else False

    def enqueue(self, data: int) -> None:
        self.linked_list.add_last(data)

    def dequeue(self) -> None:
        self.linked_list.remove_first()

    def peek(self) -> int:
        return self.linked_list.head.data if self.linked_list is not None else None

