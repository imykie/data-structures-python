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


class QueueArr:
    def __init__(self):
        self.data = []

    def is_empty(self):
        return False if self.data.size > 0 else False

    def enqueue(self, data: int) -> None:
        self.data.append(data)

    def dequeue(self) -> None:
        self.data.pop(0)

    def peek(self) -> int:
        return self.data[0] if len(self.data) > 0 else None

