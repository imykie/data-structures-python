"""
DisjoinSet - Quick Find
Find -> O(1)
Union -> O(n)
Connected -> O(1)
"""

class QuickFind:
    def __init__(self, size: int) -> None:
        self.size = size
        self.root = [0] * self.size

        for i in range(self.size):
            self.root[i] = [i]

    def find(self, x: int) -> int:
        return self.root[x]

    def union(self, x: int, y: int) -> None:
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            for i in range(self.size):
                if self.root[i] == root_y:
                    self.root[i] = root_x


    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

