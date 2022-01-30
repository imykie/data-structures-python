class HashMap:
    def __init__(self, size=1000):
        self.size = size
        self.data = [None] * self.size

    def put(self, key: int, value: int) -> None:
        pos = self.hash(key)

        if self.data[pos] is None:
            self.data[pos] = ListNode(key, value)
            return

        next_node = self.data[pos]
        self.data[pos] = ListNode(key, value, next_node)
        return

    def get(self, key: int) -> int:
        pos = self.hash(key)
        if self.data[pos] is None:
            return -1
        head = self.data[pos]
        while head:
            if head.key == key:
                return head.value
            head = head.next
        return -1

    def remove(self, key: int) -> None:
        pos = self.hash(key)
        current = self.data[pos]
        if current is None:
            return
        if current.key == key:
            self.data[pos] = current.next
            return
        prev, current = current, current.next
        while current:
            if current.key == key:
                prev.next = current.next
                return
            prev, current = current, current.next
        return

    def clear(self) -> None:
        self.data = [None] * self.size

    def hash(self, key):
        return key % self.size


class ListNode:
    def __init__(self, key, value, next_node=None):
        self.key = key
        self.value = value
        self.next = next_node
