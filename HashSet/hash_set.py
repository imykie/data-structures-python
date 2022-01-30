class HashSet:
    def __init__(self, size=1000):
        self.size = size
        self.data = [None] * self.size

    def add(self, key: int, value: int) -> None:
        pos = self.hash(key)

        if self.data[pos] is None:
            self.data[pos] = ListNode(key, value)
            return

        next_node = self.data[pos]
        self.data[pos] = ListNode(key, next_node)
        return

    def remove(self, key: int) -> None:
        pos = self.hash(key)
        head = self.data[pos]
        if not head:
            return
        if head.key == key:
            self.data[pos] = head.next
        prev = head
        while head:
            if head.key == key:
                prev.next = head.next
                return
            prev, head = head, head.next
        return

    def contains(self, key: int) -> bool:
        pos = self.hash(key)
        head = self.data[pos]
        if not head:
            return False
        if head.key == key:
            return True
        while head:
            if head.key == key:
                return True
            head = head.next
        return False

    def clear(self) -> None:
        self.data = [None] * self.size

    def hash(self, key: int):
        return key % self.size


class ListNode:
    def __init__(self, key, next_node=None):
        self.key = key
        self.next = next_node
