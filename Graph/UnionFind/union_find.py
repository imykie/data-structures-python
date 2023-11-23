"""
This is the optimized union find with path compression and union by rank
Find -> O(α(N))
Union -> O(α(N))
Connected -> O(α(N))

For N operations, the amortized time complexity of the union-find algorithm (using path compression with union by rank) is O(α(N)). 
Here, α(N) is the inverse Ackermann function that grows so slowly, that it doesn't exceed 4 for all reasonable N (approximately N < 10^600) 
"""

class UnionFind:
    def __init__(self, size: int) -> None:
        self.size = size
        self.root = [i for i in range(self.size)]
        self.rank = [1] * self.size


    def find(self, x: int) -> int:
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]


    def union(self, x: int, y: int) -> None:
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False

        if self.rank[root_x] > self.rank[root_y]:
            self.root[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.root[root_x] = root_y
        else:
            self.root[root_y] = root_x
            self.rank[root_x] += 1

        return True
    

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
