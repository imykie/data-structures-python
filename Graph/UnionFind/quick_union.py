"""
UnionFind - Quick Union
Worst case scenario time complexity
Find -> O(n)
Union -> O(n)
Connected -> O(n)

Generally, Quick Union is more efficient than Quick Find
"""

class QuickUnion:
    def __init__(self, size: int) -> None:
        self.size = size
        self.root = [i for i in range(self.size)]


    def find(self, x: int) -> int:
        while x != self.root[x]:
            x = self.root[x]
        return x


    def union(self, x: int, y: int) -> None:
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.root[root_y] = root_x


    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)