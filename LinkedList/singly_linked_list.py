from __future__ import annotations
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
        self.size += 1

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
        if self.head is not None:
            if self.head.data == data:
                self.remove_first()
                return
            if self.tail.data == data:
                self.remove_last()
                return
            current = self.head
            prev = None
            while current.next is not None:
                if current.data == data:
                    prev.next = current.next
                prev = current
                current = current.next
            self.size -= 1
            return
        return

    # position index starts from 0
    def remove_at_position(self, pos: int) -> None:
        if self.head is not None:
            if pos >= self.size:
                raise ValueError('Linked list size exceeded')
            if pos == 0:
                self.remove_first()
                return
            if pos == self.size - 1:
                self.remove_last()
                return
            current = self.head
            prev = None
            for i in range(self.size):
                if i == pos:
                    prev.next = current.next
                    break
                prev = current
                current = current.next
            self.size -= 1
            return
        return

    def contains(self, data: int) -> bool:
        if self.head is not None:
            current = self.head
            while current is not None:
                if current.data == data:
                    return True
                current = current.next
        return False

    def insert(self, data: int, pos: int) -> None:
        if self.head is not None:
            if pos >= self.size + 1:
                raise ValueError('invalid position - cannot add to a position greater than the linkedlist size')
            if pos == 0:
                self.add_first(data)
                return
            if pos == self.size:
                self.add_last(data)
                return
            node = Node(data)
            # set current to index 1
            current = self.head.next
            prev = self.head
            for i in range(1, self.size):
                if i == pos:
                    prev.next = node
                    node.next = current
                    break
                prev = current
                current = current.next
            self.size += 1
        return

    def replace(self, data: int, pos) -> None:
        if self.head is not None:
            if pos >= self.size:
                raise ValueError('invalid position - cannot replace node data because node does not exist')
            if pos == 0:
                self.head.data = data
                return
            if pos == self.size - 1:
                self.tail.data = data
                return
            # set current to index 1
            current = self.head.next
            prev = self.head
            for i in range(1, self.size):
                if i == pos:
                    current.data = data
                    break
                prev = current
                current = current.next
        return

    # returns -1 if position not found
    def find(self, data: int) -> int:
        if self.head is not None:
            pos = 0
            current = self.head
            while current is not None:
                if current.data == data:
                    return pos
                current = current.next
                pos += 1
        return -1

    def display(self) -> None:
        if self.head is not None:
            current = self.head
            for i in range(self.size):
                if i == self.size - 1:
                    print(str(current.data), end='')
                else:
                    print(str(current.data)+' -> ', end='')
                current = current.next
        return

    def reverse(self) -> None:
        if self.head is not None:
            if self.head == self.tail:
                return
            current = self.head
            prev = None
            while current is not None:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            self.tail = self.head
            self.head = prev
        return

    def no_of_occurrence(self, data: int) -> None:
        counter = 0
        if self.head is not None:
            current = self.head
            while current is not None:
                if current.data == data:
                    counter += 1
                current = current.next
        return counter
