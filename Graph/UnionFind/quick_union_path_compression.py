"""
Find -> O(logn)
Union -> O(logn)
Connected -> O(logn)
"""
class QuickUnionPathCompression:
    def __init__(self, size: int) -> None:
        self.size = size
        self.root = [i for i in range(self.size)]


    def find(self, x: int) -> int:
        while x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]


    def union(self, x: int, y: int) -> None:
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.root[root_y] = root_x


    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)