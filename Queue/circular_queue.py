from __future__ import annotations


class CircleQueue:
    def __init__(self, max_size) -> None:
        self.size = self.head = self.tail = 0
        self.max_size = max_size
        self.queue = [None] * self.max_size

    def enqueue(self, data: int) -> bool:
        if self.is_full():
            raise ValueError('Queue is full')
        self.queue[self.tail] = data
        self.tail = (self.tail + 1) % self.max_size
        self.size += 1
        return True

    def dequeue(self) -> int:
        if self.is_empty():
            raise ValueError('Queue is empty')
        temp = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        return temp

    def front(self) -> int:
        return self.queue[self.head]

    def rear(self) -> int:
        return self.queue[self.tail - 1]

    def is_full(self) -> bool:
        return self.size == self.max_size

    def is_empty(self) -> bool:
        return self.size == 0

    def clear(self) -> None:
        self.queue = [None] * self.max_size
        self.size = self.head = self.tail = 0

    def display(self) -> None:
        print(
            f"queue: {self.queue}, max size: {self.max_size}, current size: {self.size} head: {self.head}, tail: {self.tail}")
